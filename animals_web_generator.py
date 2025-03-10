from data_loader import load_data, get_available_skin_types
from animals_logic import fetch_animal_data
from file_utils import replace_animal_repository

def main():
    # 1) Gather all distinct skin_type values
    possible_skin_types = get_available_skin_types("files/animals_data.json")

    # 2) Display them to the user
    print("Available skin types:")
    for i, stype in enumerate(possible_skin_types, start=1):
        print(f"{i}. {stype}")

    # 3) Prompt user for a skin_type
    chosen_skin_type = None
    while chosen_skin_type is None:
        try:
            choice = int(input("\nEnter the number of the skin type you want to view: "))
            if 1 <= choice <= len(possible_skin_types):
                chosen_skin_type = possible_skin_types[choice - 1]
            else:
                print("Invalid selection. Please enter a valid number from the list.")
        except ValueError:
            print("Please enter a valid integer choice.")

    # 4) Load the animal data and generate HTML for only animals that have the chosen skin_type
    data = load_data("files/animals_data.json")
    animal_characteristic = fetch_animal_data(data, selected_skin_type=chosen_skin_type)

    # 5) Insert the generated HTML into the template
    replace_animal_repository(
        "files/animals.template.html",
        "__REPLACE_ANIMALS_INFO",
        animal_characteristic
    )

    #Let the user know the operation is complete
    print(f"\nSuccessfully generated 'animals.html' for skin type: {chosen_skin_type}")


if __name__ == "__main__":
    main()
