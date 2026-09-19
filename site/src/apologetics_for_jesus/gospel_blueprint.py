from flask import Blueprint, render_template

blueprint = Blueprint('gospel', __name__, static_folder='static/gospel')

# Cache will be injected by main.py
cache = None

def init_cache(cache_instance):
    """Initialize cache from main.py"""
    global cache
    cache = cache_instance

@blueprint.route('/')
def home():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='gospel_home')
        def _cached():
            return render_template("gospel/home.html")
        return _cached()
    return render_template("gospel/home.html")

@blueprint.route('/what-is-the-gospel')
def gospel_message():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='gospel_message')
        def _cached():
            return render_template("gospel/gospel_message.html")
        return _cached()
    return render_template("gospel/gospel_message.html")

@blueprint.route('/fulfilled-prophecy')
def prophecy():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='gospel_prophecy')
        def _cached():
            return render_template("gospel/prophecy.html")
        return _cached()
    return render_template("gospel/prophecy.html")

@blueprint.route('/resurrection')
def resurrection():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='gospel_resurrection')
        def _cached():
            return render_template("gospel/resurrection.html")
        return _cached()
    return render_template("gospel/resurrection.html")

@blueprint.route('/sources')
def references():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='gospel_references')
        def _cached():
            return render_template("gospel/references.html")
        return _cached()
    return render_template("gospel/references.html")
