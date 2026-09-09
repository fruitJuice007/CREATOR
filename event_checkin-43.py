# === Stage 43: Добавь пагинацию длинных списков ===
# Project: EventCheckin
def paginate_list(items: list, page: int = 1, page_size: int = 20) -> dict:
    """Возвращает пагинацию списка.

    Args:
        items: список элементов.
        page: номер страницы (начинается с 1).
        page_size: количество элементов на странице.

    Returns:
        словарь с пагинационными данными.
    """
    total_pages = (len(items) + page_size - 1) // page_size
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_items = items[start_index:end_index]
    return {
        "items": paginated_items,
        "total_items": len(items),
        "current_page": page,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }
