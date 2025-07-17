# 📄 AI Resume Ranker

**AI Resume Ranker** is a Streamlit-based application that automatically ranks multiple resumes (PDFs) against a provided job description using keyword matching and scoring logic for **skills**, **education**, and **experience**.

---

## 🚀 Features

- Upload and process multiple PDF resumes
-  Paste job description to extract relevant keywords
-  Extract **contact info**, **matched skills**, **education**, **experience**, and **summary**
-  Score each resume out of 100
-  Download ranked leaderboard as Excel
-  Visualize score distribution (optional)

---

## 📊 Scoring Criteria

| Category       | Weight | Description |
|----------------|--------|-------------|
| Skills         | 40     | Based on matched job description keywords |
| Education      | 20     | Matched from keywords like "B.Tech", "M.Sc", etc. |
| Experience     | 40     | Matched from words like "intern", "project", "developer" |

---

## 🧠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend Logic**: `PyPDF2`, `re`, `pandas`, `openpyxl`
- **Excel Export**: `BytesIO`, `pandas`
- **Language**: Python 3.9+

---

## 🛠 Installation

1. **Clone the repo**
   
   git clone https://github.com/your-username/ai-resume-ranker.git
   cd ai-resume-ranker
   
 2.**Create a virtual environment**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.**Install dependencies**

pip install -r requirements.txt

4.**Run the app**


streamlit run streamlit_app.py

**Sample Job Description**

We are looking for a software developer with experience in Python, Django, REST APIs,
SQL, and strong problem-solving skills. Candidates should have a Bachelor's in Computer Science.

 **Output**
 
Resume summaries and scores displayed in Streamlit

Downloadable Excel leaderboard of all ranked resumes
