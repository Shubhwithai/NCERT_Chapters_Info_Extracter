from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class LearningObjective(BaseModel):
    objective: str = Field(description="The learning objective statement")
    description: str = Field(description="A brief description of the learning objective")

class KeyConcept(BaseModel):
    concept: str = Field(description="The key concept or topic")
    explanation: str = Field(description="A brief explanation of the key concept")

class ContentSection(BaseModel):
    title: str = Field(description="The title of the content section")
    content: str = Field(description="The main content of the section")

class RealLifeExample(BaseModel):
    example: str = Field(description="The real-life example or application")
    explanation: str = Field(description="An explanation of how the example relates to the topic")

class Exercise(BaseModel):
    question: str = Field(description="The exercise question")
    solution: str = Field(description="The step-by-step solution to the exercise question")
    difficulty_level: str = Field(description="The difficulty level of the exercise (e.g., easy, medium, hard)")

class NCERTChapter(BaseModel):
    chapter_title: str = Field(description="The title of the NCERT chapter")
    subject: str = Field(description="The subject or domain of the chapter")
    grade_level: str = Field(description="The grade level or standard for which the chapter is intended")
    chapter_overview: str = Field(description="An overview or introduction to the chapter")
    learning_objectives: List[LearningObjective] = Field(description="The learning objectives of the chapter")
    key_concepts: List[KeyConcept] = Field(description="The key concepts covered in the chapter")
    content_sections: List[ContentSection] = Field(description="The main content sections of the chapter")
    real_life_examples: List[RealLifeExample] = Field(description="Real-life examples related to the chapter content")
    exercises: List[Exercise] = Field(description="Practice exercises for students")
    summary: str = Field(description="A summary of the key points from the chapter")
    additional_resources: List[str] = Field(description="Additional resources for further learning")
