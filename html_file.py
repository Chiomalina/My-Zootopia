from animals_web_generator import main, fetch_animal_data



with open("files/animals.template.html", mode="r") as fileobject:
	animal_data = fileobject.read()


	replaced_animal_info = data.replace(___REPLACE_ANIMALS_INFO__, animal_data)
