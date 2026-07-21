📖 Overview

Recruiters often spend significant time manually reviewing resumes. This project automates the process by combining PDF text extraction with an LLM to transform unstructured resume text into structured data.

The entire application runs locally using Ollama, ensuring complete privacy without requiring any external APIs or cloud services.

✨ Features
Upload resumes in PDF format
Automatic text extraction using pypdf
Structured information extraction using Llama 3.2 (Ollama)
Extracts:
Name
Email
Phone Number
Skills
Education
Experience
Projects
Certifications
Dynamic result rendering using Jinja2 templates
Fully offline and privacy-friendly
Lightweight FastAPI backend
🛠 Tech Stack
Python
FastAPI
Ollama
Llama 3.2
pypdf
Jinja2
HTML
Tailwind CSS
JavaScript

📁 Project Structure
AI-Resume-Parser/
│
├── templates/
│   └── index.html
│
├── images/
│   ├── homepage.png
│   ├── upload.png
│   ├── output.png
│   └── result.png
│
├── __DATA__/
│   └── .gitkeep
│
├── app.py
├── resumeparser.py
├── requirements.txt
├── README.md
├── .gitignore

⚙️ Installation
1. Clone the repository

2. Install dependencies
pip install -r requirements.txt

3. Install Ollama

Download and install Ollama from:

https://ollama.com

4. Pull the model
ollama pull llama3.2

5. Start Ollama
ollama serve

6. Run the application
python app.py

Open:

http://127.0.0.1:8000

📸 Application Workflow
Upload a PDF resume.
Extract text using pypdf.
Send extracted text to Llama 3.2 through Ollama.
Receive structured JSON output.
Display the extracted information on the webpage.
📸 Project Preview
Homepage
![Homepage](images/homepage.png)
Upload Resume
![Upload Resume](images/upload.png)
Parsed Output
![Output](images/output1.png)
Structured Result
![Result](images/output2.png)

🚀 Future Improvements
Resume-to-job description matching
ATS compatibility score
Support DOCX resumes
Export results as CSV or JSON
User authentication
Cloud deployment
Multiple LLM support (OpenAI, Gemini, Claude)

🙏 Acknowledgements
Ollama
Meta Llama 3.2
FastAPI
pypdf

👩‍💻 Author

Vaanya Mathur

B.Tech in Computer Science & Engineering (AI & ML)