import os
import sys
from utils import download_xml, read_xml_content, extract_text_from_xml


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py https://www.legislation.gov.uk/path/to/xml")
        sys.exit(1)

    url = sys.argv[1]

    if not os.path.exists("data"):
        os.makedirs("data")

    # Create a filename based on the URL
    filename = (
        url.split("https://www.legislation.gov.uk/")[1].split("?")[0].replace("/", "_")
    )

    xml_path = f"data/{filename}.xml"
    txt_path = f"data/{filename}.txt"

    # Download and process XML
    download_xml(url, xml_path)
    xml_content = read_xml_content(xml_path)
    text = extract_text_from_xml(xml_content)

    # Save the cleaned text
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved cleaned text to {txt_path}")


if __name__ == "__main__":
    main()
