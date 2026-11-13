# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: EventCheckin
CUSTOM_VIEWS = {}

def add_custom_view(view_id, name, description, default_filter=None, columns=None):
    CUSTOM_VIEWS[view_id] = {
        "id": view_id,
        "name": name,
        "description": description,
        "default_filter": default_filter,
        "columns": columns,
        "created_at": time.time(),
        "used_by": {},
    }

def list_custom_views():
    return list(CUSTOM_VIEWS.values())

def get_custom_view(view_id):
    return CUSTOM_VIEWS.get(view_id)

def delete_custom_view(view_id):
    return CUSTOM_VIEWS.pop(view_id, None)

def use_custom_view(view_id, list_id):
    view = CUSTOM_VIEWS.get(view_id)
    if view:
        view["used_by"][list_id] = view["used_by"].get(list_id, 0) + 1
