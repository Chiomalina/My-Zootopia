def replace_animal_repository(html_file, old_text, new_text, output_file="animals4.html"):
    """
    Reads the HTML file, replaces the first occurrence of old_text with new_text,
    and writes the result to the output_file.
    """
    with open(html_file, mode="r", encoding="utf-8") as fileobject:
        file_content = fileobject.read()

    replaced_animal_info = file_content.replace(old_text, new_text, 1)

    with open("animals.html", mode="w", encoding="utf-8") as fileobject:
        fileobject.write(replaced_animal_info)
