import re
import PyPDF2
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from Modelss import NCERTChapter
import pandas as pd
from langchain_openai import ChatOpenAI


def read_pdf(file):
    """
    Reads a PDF file and extracts text from it.
    :param file: File object
    :return: String
    """
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    text = ""
    for i in range(num_pages):
        page = reader.pages[i]
        text += page.extract_text()
    return text


def extract_info(NCERTChapter_text: str, model):
    """
    Extracts sections from the NCERT Chapter text using the LLM.
    :param NCERTChapter_text: Text from the NCERT chapter
    :param model: Language model to use for extraction
    :return: Extracted information in structured format
    """
    parser = OutputFixingParser.from_llm(parser=PydanticOutputParser(pydantic_object=NCERTChapter), llm=model)
    format_instructions = parser.get_format_instructions()
    extracted_text = model.predict(
        f"Given an NCERT Book Chapter text: {NCERTChapter_text}, extract all the relevant sections as per the format. \n {format_instructions}"
    )
    extracted_info = parser.parse(extracted_text)
    return extracted_info


def resume_to_dataframe(NCERTChapter_info: NCERTChapter) -> pd.DataFrame:
    data = {
        "chapter_title": NCERTChapter_info.chapter_title,
        "subject": NCERTChapter_info.subject,
        "grade_level": NCERTChapter_info.grade_level,
        "chapter_overview": NCERTChapter_info.chapter_overview,
        "learning_objectives": [lo.dict() for lo in NCERTChapter_info.learning_objectives],
        "key_concepts": [kc.dict() for kc in NCERTChapter_info.key_concepts],
        "content_sections": [cs.dict() for cs in NCERTChapter_info.content_sections],
        "real_life_examples": [re.dict() for re in NCERTChapter_info.real_life_examples],
        "exercises": [ex.dict() for ex in NCERTChapter_info.exercises],
        "summary": NCERTChapter_info.summary,
        "additional_resources": NCERTChapter_info.additional_resources
    }
    return pd.json_normalize(data)
