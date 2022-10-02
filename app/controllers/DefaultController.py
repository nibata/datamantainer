from flask import render_template, redirect, url_for, request, abort, flash, current_app


def index():
    current_app.logger.info("HELLO WORLD!")
    return render_template('Views/default/index.html')