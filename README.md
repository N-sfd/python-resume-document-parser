# Python Resume & Document Parser

This project extracts structured data from resumes and documents (PDF/DOCX)
and outputs clean JSON for ATS or automation use cases.

## Features
- Resume parsing
- Text cleaning
- Structured JSON output
- Easy to extend

## Input
PDF / DOCX

## Output
JSON
{
  "name": "John Doe",
  "skills": ["Python", "SQL", "NLP"],
  "experience": [
    {
      "company": "ABC Corp",
      "role": "Software Engineer",
      "years": 3
    }
  ]
}


## Use Cases
- ATS systems
- HR automation
- Document processing

## Demo
(Input screenshot)
(Output JSON screenshot)

## How to run
```bash
python parser.py input_resume.pdf
Again — optional, but helps technical reviewers.


