# pgo.html pgowp.html replacements.txt
import argparse
import re

def replace_strings_in_file(input_file_path, output_file_path, replacements):
    # Open the file and read the content
    with open(input_file_path, encoding='utf-8') as file:
        content = file.read()

    # Iterate over the replacements and replace them
    for old, new in replacements.items():
        content = re.sub(old, new, content)

    # Write the modified content to the new file
    with open(output_file_path, 'w') as file:
        file.write(content)

def load_replacements(file_path):
    # Load the replacements from the file
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()

    # Create a dictionary from the lines
    replacements = {lines[i].strip(): lines[i + 1].strip() for i in range(0, len(lines), 2)}

    return replacements

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Replace strings in a file")

    # Add the arguments
    parser.add_argument('input_file_path', type=str, help='The path to the input file')
    parser.add_argument('output_file_path', type=str, help='The path to the output file')
    parser.add_argument('replacements_file_path', type=str, help='The path to the replacements file')

    # Parse the arguments
    args = parser.parse_args()

    # Load the replacements
    replacements = load_replacements(args.replacements_file_path)

    # Call the function to replace the strings in the file
    replace_strings_in_file(args.input_file_path, args.output_file_path, replacements)

if __name__ == "__main__":
    main()
