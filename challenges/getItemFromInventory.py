def get_item_at_index(items, index):
    size = len(items) -1
    if index < 0:
        return "Index out of range"
    elif index >= len(items):
        return "Index out of range"
    get_item = items[index]
    return get_item
