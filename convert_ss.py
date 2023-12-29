import os
from bs4 import BeautifulSoup
import html2text

def convert_html_to_md(file_path):
    # Read the HTML file
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted parts of the HTML like header, sidebar, footer
    unwanted_tags = ['header', 'footer', 'sidebar']
    for tag in unwanted_tags:
        for match in soup.findAll(tag):
            match.decompose()

    # Convert the cleaned HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = True
    markdown_content = h.handle(str(soup))

    # Save the Markdown content to a file
    md_file_path = os.path.splitext(file_path)[0] + '.md'
    with open(md_file_path, 'w') as md_file:
        md_file.write(markdown_content)

# Directory containing the HTML files
dir_path = 'docs/polygon_forex_docs'

# Convert all HTML files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        file_path = os.path.join(dir_path, filename)
        convert_html_to_md(file_path)