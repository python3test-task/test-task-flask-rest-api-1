from app.api import bp
from flask import jsonify
from app.models import Post
from flask import request
from flask import url_for
from app import db
from app.api.errors import bad_request
from app.api.auth import token_auth
from flask import g


@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    return jsonify(Post.query.get_or_404(id).to_dict())


@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    data = [post.to_dict() for post in posts]
    return jsonify(data)


@bp.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    data = request.get_json() or {}
    if 'body' not in data:
        return bad_request('must include body fields')
    # присваеваем посту id пользователя который его создает
    data['user_id'] = g.current_user.id
    post = Post()
    post.from_dict(data)  
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response


@bp.route('/posts/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json() or {}
    if 'body' not in data:
        return bad_request('must include body fields')
    # только владелец может обновить пост
    if post.user_id != g.current_user.id:
        return bad_request('you do not have permission to update this post.')
    data['user_id'] = g.current_user.id
    post.from_dict(data)
    db.session.commit()
    return jsonify(post.to_dict())


@bp.route('/posts/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    # только владелец может удалить пост
    if post.user_id != g.current_user.id:
        return bad_request('you do not have permission to delete this post.')
    db.session.delete(post)
    db.session.commit()
    # после удаления выводим все оставшиеся посты
    posts = Post.query.all()
    data = [post.to_dict() for post in posts]
    response = jsonify(data)
    response.status_code = 202
    response.headers['Location'] = url_for('api.get_posts')
    return response

