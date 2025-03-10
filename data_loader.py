import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, mode="r", encoding="utf-8") as handle:
        return json.load(handle)

def get_available_skin_types(file_path):
    """
    Returns a sorted list of all distinct skin_type values in the JSON.
    Animals missing skin_type are ignored.
    """
    data = load_data(file_path)
    skin_types_set = set()

    for animal_obj in data:
        characteristics = animal_obj.get("characteristics", {})
        actual_skin = characteristics.get("skin_type")
        if actual_skin:
            skin_types_set.add(actual_skin.lower())

    return sorted(skin_types_set)
