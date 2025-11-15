def note_to_dict(item) -> dict:
    # This will return a dictionary
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }

def note_list(items) -> list:
    # This will return a list
    return [note_to_dict(item) for item in items]