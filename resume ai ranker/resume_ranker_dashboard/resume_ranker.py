import os
import re
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_contact_info(text):
    email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    phone = re.search(r"\+?\d[\d\s\-]{9,15}", text)
    return {
        "email": email.group() if email else "Not found",
        "phone": phone.group() if phone else "Not found"
    }

def score_resume(text, job_description):
    text = text.lower()
    jd = job_description.lower()

    # Define keywords
    skills = re.findall(r"\b[a-zA-Z]+\b", jd)
    education_keywords = ["btech", "b.e", "bachelor", "engineering", "msc", "m.tech", "computer science", "it"]
    experience_keywords = ["intern", "project", "developer", "experience", "worked", "training"]

    matched_skills = [skill for skill in skills if skill in text]
    matched_education = [edu for edu in education_keywords if edu in text]
    matched_experience = [exp for exp in experience_keywords if exp in text]

    # Weightage
    skill_score = len(matched_skills) / len(set(skills)) * 40 if skills else 0
    education_score = 20 if matched_education else 0
    experience_score = min(len(matched_experience) * 5, 40)

    total_score = round(skill_score + education_score + experience_score, 2)

    return {
        "skills_matched": matched_skills,
        "education_matched": matched_education,
        "experience_matched": matched_experience,
        "total_score": total_score
    }

def process_and_rank_resumes(resume_files, job_description):
    results = []

    for resume_file in resume_files:
        text = extract_text_from_pdf(resume_file)
        contact = extract_contact_info(text)
        scoring = score_resume(text, job_description)

        results.append({
            "filename": resume_file.name,
            "email": contact["email"],
            "phone": contact["phone"],
            "score": scoring["total_score"],
            "summary": text[:300] + "...",
            "skills_matched": scoring["skills_matched"],
            "education_matched": scoring["education_matched"],
            "experience_matched": scoring["experience_matched"]
        })

    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    return sorted_results
