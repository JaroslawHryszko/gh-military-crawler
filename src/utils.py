import sys
import unicodedata
import io
from typing import List, Union

import PIL
import langdetect
from langdetect.lang_detect_exception import LangDetectException
import pytesseract
from PIL import Image
from github.ContentFile import ContentFile
from pypdf import PdfReader
from pdf2image import convert_from_bytes

from src.constants import ROOT_PROJECT_PATH


def read_keywords():
    military_names = []
    with open(ROOT_PROJECT_PATH / "data/military_names.txt", "r", encoding="utf-8") as file:
        military_names.extend(file.read().split("\n"))
    with open(ROOT_PROJECT_PATH / "data/other.txt", "r", encoding="utf-8") as file:
        military_names.extend(file.read().split("\n"))
    return military_names


def get_file_extension(file_name: str):
    parts = file_name.split(".")
    # Check if the file name starts with a dot or if there's only one part (no extension)
    if file_name.startswith(".") or len(parts) == 1:
        return None  # Return None for files like .gitignore or files without extensions
    return "." + parts[-1]  # Return the last part as the file extension


def is_cyrillic(char):
    return "CYRILLIC" in unicodedata.name(char, "")


def check_for_russian(content: str, languages: List[str] = None) -> float:
    if languages is None:
        languages = ["ru"]
    try:
        if any(
            lang in map(lambda x: x.lang, langdetect.detect_langs(content))
            for lang in languages
        ):
            return 1.0
        return 0.0
    except LangDetectException:
        return 0.0


def handle_image_file(image_file: Union[ContentFile, Image]) -> float:
    try:
        if isinstance(image_file, ContentFile):
            image_file = Image.open(io.BytesIO(image_file.decoded_content))
    except PIL.UnidentifiedImageError as e:
        print("Exception in handle_pdf_file")
        print(f"name: {image_file.name}, encoding: {image_file.encoding}")
        print(e, file=sys.stderr)
        return 0.0

    text_from_image = pytesseract.image_to_string(image_file)
    probability = 0.0
    probability += check_for_russian(text_from_image)
    return probability


def run_ocr_on_pdf(pdf_file: ContentFile):
    # TODO try ocrmypdf if this works bad
    images_from_pdf = convert_from_bytes(pdf_file.decoded_content)
    probability = 0.0
    for image in images_from_pdf:
        probability += handle_image_file(image)
    return probability / len(images_from_pdf)


def handle_pdf_file(pdf_file: ContentFile) -> float:
    try:
        pdf_handle = PdfReader(io.BytesIO(pdf_file.decoded_content))
    except Exception as e:
        print("Exception in handle_pdf_file")
        print(f"name: {pdf_file.name}, encoding: {pdf_file.encoding}")
        print(e, file=sys.stderr)
        return 0.0

    if pdf_handle.is_encrypted:
        return 0.0

    text_from_pdf = ""
    for page in pdf_handle.pages:
        text_from_pdf += page.extract_text()
        text_from_pdf += " "
    # TODO is the condition right here? should ocr be done only if text is empty?
    if text_from_pdf == "":
        run_ocr_on_pdf(pdf_file)
    probability = 0.0
    probability += check_for_russian(text_from_pdf)
    return probability
