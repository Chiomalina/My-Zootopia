def serialize_animal(animal_obj):
    """Handles the HTML serialization of a single animal object."""
    name = animal_obj.get("name", "Unknown Name")
    characteristics = animal_obj.get("characteristics", {})
    taxonomy = animal_obj.get("taxonomy", {})

    # Pull out fields safely
    diet = characteristics.get("diet", "Unknown Diet")
    locations = animal_obj.get("locations", [])
    location_str = ", ".join(locations)
    animal_type = characteristics.get("type", "N/A")
    skin_type = characteristics.get("skin_type", "Unknown")
    lifespan = characteristics.get("lifespan", "Unknown")
    weight = characteristics.get("weight", "Unknown")
    description = animal_obj.get("description", "Unknown Description")

    # Convert taxonomy dictionary into a readable string
    taxonomy_str = ", ".join(f"{key}: {value}" for key, value in taxonomy.items())

    # Build the HTML snippet for one animal
    output = f'\n<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n\n'
    output += (
        f'  <div class="card__text">'
        f'   <ul class="card__subtitle">\n'
        f'    <li><strong>Diet:</strong> {diet}</li>\n'
        f'    <li><strong>Location:</strong> {location_str}</li>\n'
        f'    <li><strong>Animal Type:</strong> {animal_type}</li>\n'
        f'    <li><strong>Lifespan:</strong> {lifespan}</li>\n'
        f'    <li><strong>Skin Type:</strong> {skin_type}</li>\n'
        f'    <li><strong>Weight:</strong> {weight}</li>\n'
        f'    <li><strong>Description:</strong> {description}</li>\n'
        f'    <li><strong>Taxonomy:</strong> {taxonomy_str}</li>\n'
        f'   </ul>\n'
        f'  </div>\n'
        f'</li>\n'
    )
    return output


def fetch_animal_data(data, selected_skin_type=None):
    """
    Filters by selected_skin_type if provided, and builds a single
    output string by calling serialize_animal for each valid animal.
    """
    concatenated_animal_data = ""

    for content in data:
        characteristics = content.get("characteristics", {})

        # If a skin_type is specified, skip animals that don't match
        if selected_skin_type is not None:
            animal_skin_type = characteristics.get("skin_type", "").lower()
            if animal_skin_type != selected_skin_type.lower():
                continue

        try:
            # Generate the HTML for a single animal and append it
            concatenated_animal_data += serialize_animal(content)

        except KeyError:
            # If any key is missing in content, skip this animal
            continue
        except Exception:
            # Catch-all for unforeseen errors
            continue

    return f"\n{concatenated_animal_data}"
