from . import root

@root.app_errorhandler(500)
def internal_server_error(e):
    return "Internal Server Error", 500

@root.app_errorhandler(404)
def page_not_found(e):
    return "Page not found", 404
