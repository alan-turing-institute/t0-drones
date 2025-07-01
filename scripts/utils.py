# make a function that given the url of a xml downloads it and saves it as an xml file
import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup


def download_xml(url: str, output_file: str) -> None:
    """
    Downloads an XML file from the given URL and saves it to the specified output file.

    Args:
        url (str): The URL of the XML file to download.
        output_file (str): The path where the XML file will be saved.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses

    with open(output_file, "wb") as f:
        f.write(response.content)

    print(f"Downloaded XML from {url} and saved to {output_file}")


def read_xml_content(file_path: str) -> str:
    """
    Reads the content of an XML file and returns it as a string.

    Args:
        file_path (str): The path to the XML file.

    Returns:
        str: The content of the XML file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        xml_content = f.read()
    return xml_content


def extract_text_from_xml(xml_content: str) -> str:
    """
    Extracts text from an XML content string.

    Args:
        xml_content (str): The XML content as a string.

    Returns:
        str: The extracted text from the XML.
    """
    soup = BeautifulSoup(xml_content, "lxml")
    # find the div named "content"
    content_div = soup.find("div", {"id": "content"})
    if not content_div:
        raise ValueError("Content div not found in the HTML.")
    # Extract the text from the content div

    # remove from text elements such as <a  of class="LegCommentaryLink"
    for link in content_div.find_all("a", class_="LegCommentaryLink"):
        link.decompose()

    text = content_div.get_text(separator="\n", strip=True)

    return text
