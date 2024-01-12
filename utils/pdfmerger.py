import os
import pdfkit
from PyPDF2 import PdfMerger
import logging

logging.basicConfig(level=logging.INFO)

def convert_html_to_pdf(source_dir, output_dir):
    """ Convert all HTML files in source_dir to PDFs in output_dir """
    options = {
        'load-error-handling': 'ignore'
    }
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if d not in ['assets', 'terms']]
        for file in files:
            if file.endswith('.html'):
                html_path = os.path.join(root, file)
                pdf_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.pdf')
                if os.path.exists(html_path):
                    try:
                        logging.info(f'Converting {html_path} to PDF...')
                        pdfkit.from_file(html_path, pdf_path, options=options)
                        logging.info(f'Successfully converted {html_path} to {pdf_path}')
                    except Exception as e:
                        logging.error(f'Error converting {html_path} to PDF: {e}')
                else:
                    logging.error(f'HTML file {html_path} does not exist')

def merge_pdfs(source_dir, output_pdf_path):
    """ Merge all PDF files in source_dir into a single PDF file """
    merger = PdfMerger()
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                if os.path.exists(pdf_path):
                    try:
                        logging.info(f'Appending {pdf_path}...')
                        merger.append(pdf_path)
                    except Exception as e:
                        logging.error(f'Error appending {pdf_path}: {e}')
                else:
                    logging.error(f'PDF file {pdf_path} does not exist')
    try:
        logging.info(f'Writing merged PDF to {output_pdf_path}...')
        merger.write(output_pdf_path)
    finally:
        merger.close()

# Paths
source_html_dir = '/Users/jonbennett/Downloads/us.sitesucker.mac.sitesucker/vectorbt.pro1/pvt_6739a1da/'  # Replace with your HTML directory path
output_pdf_dir = '/Users/jonbennett/Downloads/us.sitesucker.mac.sitesucker/vectorbt.pro1/pvt_6739a1da/pdfs/'  # Replace with your desired PDF directory path
final_pdf_path = '/Users/jonbennett/Downloads/us.sitesucker.mac.sitesucker/vectorbt.pro1/pvt_6739a1da/finalpdf/merged.pdf'  # Replace with your final PDF file path

# Convert HTML to PDF
convert_html_to_pdf(source_html_dir, output_pdf_dir)

# Merge PDFs
merge_pdfs(output_pdf_dir, final_pdf_path)