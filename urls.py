# encoding: utf-8
from views.index import index_page


def register_urls(app):
    app.register_blueprint(index_page, url_prefix='/')
