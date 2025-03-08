import json
from tkinter.font import names

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, mode="r") as handle:
        return json.load(handle)


def fetch_animal_data(file_path):
    """Obtain individual animal details and build a single output string"""
    animals_data = load_data(file_path)

	# Initialize an empty string to store all output
    concatenated_animal_data = ""

    for content in animals_data:
        characteristics = content.get("characteristics", {})

        # Skip animals where "type is missing
        if "type" not in characteristics:
            # Just continue to the next animal without adding anything to the output
            continue

        # If "type" exists, let's safely retrieve the required keys
        try:
            name = content.get("name", "Unknown Name")
            diet = characteristics.get("diet", "Unknown Diet")
            locations = content.get("locations", [])
            animal_type = characteristics.get("type", "N/A")

            # Append information to each string
            concatenated_animal_data += "\n<li class='cards_item'>"
            concatenated_animal_data += f"\nName:  {name}<br/>\n"
            concatenated_animal_data += f"Diet:  {diet}<br/>\n"
            concatenated_animal_data += f"locations:  {locations}<br/>\n"
            concatenated_animal_data += f"Type:  {animal_type}<br/>\n"
            concatenated_animal_data += "</li>\n"

        except KeyError:
            #print(f"A KeyError occurred with {content["name"]}\n")
            continue
        except Exception as e:
            #print(f"Exception {e}occurred\n")
            continue
    return f" \n {concatenated_animal_data}"


def replace_animal_repository(html_file, old_text, new_text):
	with open(html_file, mode="r", encoding="utf-8") as fileobject:
		file_content = fileobject.read()

	# Replace the h1 element of HTML file(animals.template.html) with generated python
	# string(concatenated_animal_data)
	replaced_animal_info = file_content.replace(old_text, new_text, 1)
	# Note that 1 the count argument(Which indicated "replace only the first occurrence" of old_text)

	with open("animals.html", mode="w", encoding="utf-8") as fileobject:
		fileobject.write(replaced_animal_info)



def main():

    animal_characteristic = fetch_animal_data("files/animals_data.json")
    #print(animal_characteristic)
    reviewed_html_animal_template = replace_animal_repository("files/animals.template.html", "__REPLACE_ANIMALS_INFO", animal_characteristic )
    print(reviewed_html_animal_template)

if __name__ == "__main__":
    main()

# Task 3: Replace __REPLACE_ANIMALS_INFOR with the generated string



