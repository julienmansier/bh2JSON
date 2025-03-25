import argparse
import os
import re
import json

def parse_input(input_text):
    # Initialize the result dictionary
    result = []
    temp = []

    # Split the input into sections
    sections = input_text.split('--------------------------------------------------------------------------------')

    # Combine the two split sections into one
    # and add to a new list
    for i in range(int(len(sections)/2)):
        temp = {}
        
        sect1 = sections[i*2+1]
        sect2 = sections[i*2+2]

        # Get BH Code
        temp["bhcode"]=""

        # Get Category
        temp["category"]=""

        # Get Count
        temp["count"]=""

        # Get Explaination 
        temp["explaination"]=""


        result.append(temp)

    
   # for item in temp:
       # print(item)

    return result


def main():

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process a file with an optional file path.")
    parser.add_argument("file_path", nargs="?", default="default_file.txt", help="Path to the file to process")

    # Parse arguments
    args = parser.parse_args()
    file_path = args.file_path

    # If the file path is not provided, prompt user
    if file_path == "default_file.txt" and not os.path.exists(file_path):
        # Prompt the user to enter the file path
        file_path = input("Enter the path to the input text file: ")

    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            input_text = file.read()

        # Parse input and convert to JSON
        parsed_data = parse_input(input_text)
        json_output = json.dumps(parsed_data, indent=2)

        # Output JSON output
        #with open("bh.json", "w") as out:
            #out.write(json.dumps(json_output))

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()