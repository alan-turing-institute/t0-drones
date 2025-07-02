# make a function that given the url of a xml downloads it and saves it as an xml file
import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import re


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
    # remove ... after <a> tags containing links
    xml_content = str(xml_content)
    xml_content = re.sub(r"</a>\.\.\.", "</a>", xml_content)

    soup = BeautifulSoup(xml_content, "lxml")
    # find the right div
    content_div = soup.find("div", {"id": "viewLegContents"})
    if not content_div:
        raise ValueError("Content div not found in the HTML.")

    # remove from text elements such as <a  of class="LegCommentaryLink"
    for link in content_div.find_all("a", class_="LegCommentaryLink"):
        link.decompose()
    for annotations_div in content_div.find_all("div", class_="LegAnnotations"):
        annotations_div.clear()
    for span in content_div.find_all("span", class_="LegExtentRestriction"):
        span.decompose()

    text = content_div.get_text(separator=" ", strip=True)

    return text
