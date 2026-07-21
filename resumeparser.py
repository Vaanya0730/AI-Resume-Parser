import json
import ollama

PROMPT = """
You are an expert resume parser.

Extract the resume information.

Return ONLY valid JSON.

Do NOT explain anything.
Do NOT use markdown.
Do NOT wrap the JSON in ```json.
Return nothing except the JSON object.

Format:

{
  "name":"",
  "email":"",
  "phone":"",
  "skills":[],
  "education":[],
  "experience":[],
  "projects":[],
  "certifications":[]
}
"""


def ats_extractor(resume_text):
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": PROMPT
                },
                {
                    "role": "user",
                    "content": resume_text
                }
            ]
        )

        # Get response from Ollama
        content = response["message"]["content"].strip()

        # Remove markdown code blocks if present
        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.startswith("```"):
            content = content.replace("```", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        print("\n===== RAW OLLAMA RESPONSE =====")
        print(repr(content))
        print("===============================\n")

        return content

    except Exception as e:
        print("Ollama Error:", e)

        return json.dumps({
            "error": str(e)
        })