from flask import request, jsonify, Response, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.post import Post
from database.user import User


class Create(Resource):
    @jwt_required
    def post(self):
        user_id = get_jwt_identity()

        body = request.get_json()

        if body is None:
            abort(400, "Bad request")

        user = User.query.filter_by(id=user_id).first()

        if user is None:
            abort(403, "Not found user")

        text = body.get('text')

        if text is None:
            abort(400, "Text is required")

        post = Post()

        post.user_id = user_id
        post.text = text

        post.save()
        return jsonify(post)


class List(Resource):
    def get(self):

        page = request.args.get('page')
        limit = request.args.get('limit')

        if page is None or limit is None:
            abort(400, "Bad request")

        posts = Post.query.order_by(
            Post.created_at.desc()).paginate(int(page), per_page=int(limit), error_out=True)

        return jsonify(posts.items)


class Read(Resource):
    def get(self, post_id):

        if post_id is None:
            abort(400, "Bad request")

        post = Post.query.filter_by(id=post_id).first()

        return jsonify(post)


class Remove(Resource):
    def delete(self, post_id):

        if post_id is None:
            abort(400, "Bad request")

        post = Post.query.filter_by(id=post_id).first()

        if post is None:
            abort(404, "Not found")

        post.delete()

        return abort(200, "OK")
