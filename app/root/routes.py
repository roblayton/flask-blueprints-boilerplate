from . import root

@root.route('/')
def home():
    return "Root Home", 200
