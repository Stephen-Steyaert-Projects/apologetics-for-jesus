from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__, static_folder='static', template_folder='templates')

# Cache will be injected by main.py
cache = None

def init_cache(cache_instance):
    """Initialize cache from main.py"""
    global cache
    cache = cache_instance

@blueprint.route('/')
def home():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='home')
        def _cached():
            return render_template("home.html")
        return _cached()
    return render_template("home.html")