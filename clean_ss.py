import logging
import os
import trafilatura
import glob
import zipfile

# Set up logging
logging.basicConfig(filename='trafilatura.log', level=logging.INFO)

def process_directory(input_dir, output_dir):
    # Get a list of all files in the input directory
    files = os.listdir(input_dir)

    # Get the name of the parent directory
    parent_dir_name = os.path.basename(os.path.normpath(input_dir))

    # Create a file to store all the contents
    with open(os.path.join(output_dir, f'{parent_dir_name}_ALL.txt'), 'w', encoding='utf-8') as all_file:
        for file in files:
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, file + '.txt')

            try:
                # Read the HTML file
                with open(input_file, 'r', encoding='utf-8') as f:
                    html_string = f.read()

                # Extract the main content
                text = trafilatura.extract(html_string)

                # Write the extracted content to a text file
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)

                # Write the extracted content to the combined file
                all_file.write(text)

                logging.info(f'Successfully processed file {file}')

            except Exception as e:
                logging.error(f'Error processing file {file}: {e}')

    # Remove the individual text files
    for file in glob.glob(os.path.join(output_dir, '*.txt')):
        if file != os.path.join(output_dir, f'{parent_dir_name}_ALL.txt'):
           os.remove(file)

    # Zip all HTML files and then delete them
    with zipfile.ZipFile(os.path.join(output_dir, 'html_files.zip'), 'w') as zipf:
        for file in glob.glob(os.path.join(output_dir, '*.html')):
            zipf.write(file)
            os.remove(file)

# Replace these with your actual directories
input_dir = 'docs/lightweight-charts-tutorials'
output_dir = 'docs/lightweight-charts-tutorials'

process_directory(input_dir, output_dir)
