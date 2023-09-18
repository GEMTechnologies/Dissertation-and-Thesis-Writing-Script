import os
from flask import Flask, render_template, request
from validate_prompt import validate_prompt
from openai_module import generate_content
from document_module import create_word_document
from file_module import create_folder
from openai_commands import (
    generate_intro_command,
    generate_global_background_command,
    generate_african_background_command,
    generate_east_african_background_command,
    generate_country_specific_background_command
)

app = Flask(__name__)

def generate_chapter_one_prompts(title):
    commands = {
        "Introduction": generate_intro_command(title, "South Sudan", "Juba"),
        "Global Background": generate_global_background_command(title),
        "African Background": generate_african_background_command(title),
        "East African Background": generate_east_african_background_command(title),
        "Country-Specific Background": generate_country_specific_background_command(title, "Selected Country", "Specific Case Study Info")
    }
    return commands

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_project', methods=['POST'])
def create_project():
    title = request.form.get('title')
    create_folder(title)
    chapter_one_prompts = generate_chapter_one_prompts(title)
    chapter_one_content = ""

    for subsection, section_command in chapter_one_prompts.items():
        chapter_one_content += f"\n\n{subsection}\n"  # Add subsection as a heading
        generated_section = generate_content(section_command)
        chapter_one_content += generated_section + "\n"

    chapter_one_name = "Chapter 1.docx"
    chapter_one_file_path = os.path.join(title, chapter_one_name)
    create_word_document(chapter_one_file_path, chapter_one_content)

    return "Project created successfully!"

if __name__ == '__main__':
    app.run()
