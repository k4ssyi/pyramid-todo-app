def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("todo_index", "/index")
    config.add_route("api_todo", "/api/todo")
