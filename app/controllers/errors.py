from flask import render_template


def page_not_found(e):
    return render_template('Views/error/404.html'), 404


def server_error(e):
    return render_template("Views/error/500.html"), 500
