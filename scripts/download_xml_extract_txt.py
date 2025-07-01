from utils import download_xml, read_xml_content, extract_text_from_xml
import os

# URL of the plain view of Annex IX
URL = "https://www.legislation.gov.uk/eur/2018/1139/annex/IX?view=xml"

if not os.path.exists("data"):
    os.makedirs("data")

OUTPUT_FILE = "data/annex_ix_cleaned.txt"

download_xml(URL, "data/annex_ix.xml")
xml_content = read_xml_content("annex_ix.xml")
text = extract_text_from_xml(xml_content)
# Save the cleaned text
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Saved cleaned text to {OUTPUT_FILE}")
