from bs4 import BeautifulSoup
import os

def extract_iframes_to_html(input_file_path, output_dir):
    # Read the HTML content from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    iframes = soup.find_all('iframe')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, iframe in enumerate(iframes):
        title = iframe.get('title', f'iframe-{idx}')
        sanitized_title = ''.join(c if c.isalnum() or c in '-_ ' else '_' for c in title).strip()
        output_file_path = os.path.join(output_dir, f'{sanitized_title}.html')

        iframe_html = str(iframe)

        # Compose the new standalone HTML document
        standalone_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title> 
</head>
<body>
  {iframe_html}
</body>
</html>
"""

        # Write the HTML content to a new file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(standalone_html)

        print(f"Extracted iframe '{title}' to {output_file_path}")

if __name__ == "__main__":
    # Define input HTML file and output directory
    input_html_file = 'index.html'     # Replace with your input file path
    output_directory = 'iframes'       # Replace with your desired output directory
    extract_iframes_to_html(input_html_file, output_directory)
