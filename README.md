# NCERT_Chapters_Info_Extracter - NCERT_Chapters_Info To CSV Converter

This is a Streamlit application that allows you to convert PDF NCERT_Chapters_Info into a CSV format for easy data analysis and management. The app leverages OpenAI's language model to extract relevant information from the resumes and presents it in a structured manner.

## Features

- Upload multiple PDF  (up to 10 at a time)
- Extract key information from resumes, including chapter_title ,subject, grade_level, chapter_overview, learning_objectives, key_concepts, and more
- View the extracted resume data in a user-friendly JSON format
- Download the combined resume data as a CSV file for further analysis or processing

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/resume-to-csv.git
```

2. Install the required dependencies:

```bash
cd resume-to-csv
pip install -r requirements.txt
```

3. Set up the OpenAI API key:

Create a secrets.toml file in the project root directory with the following content:

```bash
OPENAI_API_KEY = "your_openai_api_key_here"
```
Replace "your_openai_api_key_here" with your actual OpenAI API key.

4. Usage

1. Start the Streamlit app:

```bash
streamlit run app.py
```

2. The app will open in your default web browser. Follow the on-screen instructions to upload PDF resumes and convert them to CSV format.

# Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

# License 

This project is licensed under the MIT License.

# Acknowledgments

Streamlit for the user-friendly app development framework

OpenAI for their powerful language model

LangChain for the integration with OpenAI's language model

