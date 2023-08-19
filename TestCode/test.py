import docx
from docxtpl import DocxTemplate

# Load the template .docx file
template_path = "D:\PROJECTS\PythonSockets\ETH\AutoMation\AutoMateFillingDocx\TestCode\simple_job_application_email.docx"  # Replace with the actual template file path
docs = docx.Document(template_path)
template_text = "\n".join([paragraph.text for paragraph in docs.paragraphs])

data = {
    "(Recipient's name)": "John Doe",
    "(job name)": "Software Developer",
    "(a CV, resume, cover letter, etc.)": "my resume",
    "(insert details)": "at john.doe@example.com",
    "(Your name)": "Jane Smith",
}

for placeholder, value in data.items():
    template_text = template_text.replace(placeholder, value)

output_path = "output_document.txt"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(template_text)
print("Template filled and saved.")
