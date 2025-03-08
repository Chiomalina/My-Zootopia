import json
from tkinter.font import names


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, mode="r") as handle:
        return json.load(handle)




def fetch_animal_data(file_path):
    """Obtain individual animal details"""
    animals_data = load_data(file_path)

    for content in animals_data:
        try:
            #print(content)
            name = content["name"]
            diet = content["characteristics"]["diet"]
            locations = content["locations"]
            type = content["characteristics"]["type"]
            print(f"Name: {name}\nDiet: {diet}\nLocation: {locations}\nType: {type}\n")
        except KeyError:
            print(f"A KeyError occurred with {content["name"]}\n")
        except Exception as e:
            print(f"Exception {e}occurred\n")



def main():

    animal_characteristic = fetch_animal_data("files/animals_data.json")
    print(animal_characteristic)

if __name__ == "__main__":
    main()


