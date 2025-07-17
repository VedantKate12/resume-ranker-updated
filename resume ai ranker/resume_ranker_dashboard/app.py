import streamlit as st
import pandas as pd
from io import BytesIO
from resume_ranker import process_and_rank_resumes

st.set_page_config(page_title="AI Resume Ranker", layout="wide")
st.title("📄 AI Resume Ranker")

# Input for job description
job_description = st.text_area("🔍 Paste Job Description Here", height=200)

# Upload resumes
uploaded_files = st.file_uploader(
    "📤 Upload Resumes (PDFs only)", 
    type=["pdf"], 
    accept_multiple_files=True
)

# Rank resumes on button click
if st.button("🚀 Rank Resumes"):
    if not job_description or not uploaded_files:
        st.warning("Please provide both a job description and resumes.")
    else:
        with st.spinner("Processing resumes..."):
            results = process_and_rank_resumes(uploaded_files, job_description)

        for res in results:
            st.subheader(res["filename"])
            st.write(f"**Email:** {res['email']} | **Phone:** {res['phone']}")
            st.write(f"**Score:** {res['score']} / 100")
            st.write(f"**Skills Matched:** {', '.join(res['skills_matched'])}")
            st.write(f"**Education Matched:** {', '.join(res['education_matched'])}")
            st.write(f"**Experience Matched:** {', '.join(res['experience_matched'])}")
            st.write("**Summary:**")
            st.info(res["summary"])
            st.markdown("---")

        # ✅ Generate Excel leaderboard
        if results:
            leaderboard_df = pd.DataFrame([{
                "Filename": res["filename"],
                "Email": res["email"],
                "Phone": res["phone"],
                "Score": res["score"],
                "Skills Matched": ", ".join(res["skills_matched"]),
                "Education Matched": ", ".join(res["education_matched"]),
                "Experience Matched": ", ".join(res["experience_matched"]),
                "Summary": res["summary"]
            } for res in results])

            # Sort by score descending and then by filename
            leaderboard_df = leaderboard_df.sort_values(by=["Score", "Filename"], ascending=[False, True])

            # Save to Excel in memory
            excel_file = BytesIO()
            leaderboard_df.to_excel(excel_file, index=False, sheet_name="Leaderboard")
            excel_file.seek(0)

            # Provide download button
            st.download_button(
                label="📥 Download Leaderboard as Excel",
                data=excel_file,
                file_name="Resume_Leaderboard.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
