import os
import shutil
import logging
from bs4 import BeautifulSoup
import glob
import zipfile
import time

# Set up logging
logging.basicConfig(filename='slurp.log', level=logging.WARNING)

# Define the directory path
directory = '/Users/jonbennett/Downloads/us.sitesucker.mac.sitesucker/vectorbt.pro/pvt_6739a1da/cookbook/plotting'

def process_directory(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    print(f"Found {len(files)} files in {directory}")

    # Get the name of the parent directory
    parent_dir_name = os.path.basename(os.path.normpath(directory))

    # Create a file to store all the contents
    with open(os.path.join(directory, f'{parent_dir_name}_ALL.txt'), 'w', encoding='utf-8') as all_file:
        for file in files:
            input_file = os.path.join(directory, file)
            output_file = os.path.join(directory, file + '.txt')

            try:
                # Read the HTML file
                with open(input_file, 'r', encoding='utf-8') as f:
                    html_string = f.read()

                # Parse the HTML content
                soup = BeautifulSoup(html_string, 'html.parser')

                # Extract the main text content and code blocks
                text = ' '.join(p.text for p in soup.find_all(['p', 'pre', 'code']))

                print(f"Extracted text from {file}: {text}")

                # Write the extracted content to a text file
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)

                # Write the extracted content to the combined file
                all_file.write(text)

                print(f"Successfully processed file {file}")

            except Exception as e:
                logging.error(f'Error processing file {file}: {e}')
                print(f"Error processing file {file}: {e}")

    # Zip all HTML files and then delete them
    with zipfile.ZipFile(os.path.join(directory, 'html_files.zip'), 'w') as zipf:
        for file in glob.glob(os.path.join(directory, '*.html')):
            zipf.write(file)  # Keep the original HTML files

# Iterate through the directory tree
for root, dirs, files in os.walk(directory, topdown=False):
    # Get a list of all HTML files in the current directory
    html_files = [f for f in files if f.endswith('.html')]

    # Iterate through the list of HTML files and move them to the 'api' level
    for html_file in html_files:
        old_file_path = os.path.join(root, html_file)
        if root != directory:
            new_file_name = f"{os.path.basename(root)}_{html_file}"
            new_file_path = os.path.join(directory, new_file_name)

            # Only rename if the file doesn't already exist in the destination directory
            if not os.path.exists(new_file_path):
                os.rename(old_file_path, new_file_path)

# After all files have been moved, process the directory
process_directory(directory)
