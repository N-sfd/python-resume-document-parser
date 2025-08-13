import streamlit as st
from modules.resume_parser import parse_pdf
from modules.reviewer import get_feedback, match_resume_to_job
from modules.analytics import extract_metrics, to_dataframe
from modules.exporter import export_csv
# from modules.visualization import plot_match_score_trend, plot_missing_keyword_frequency

st.title("🧠 Smart Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded_file:
    resume_text = parse_pdf(uploaded_file)
    st.subheader("Parsed Resume")
    st.text(resume_text[:500] + "...")

    with open("prompts/base_prompt.txt") as f:
        prompt_template = f.read()

    feedback = get_feedback(resume_text, prompt_template)
    st.subheader("LLM Feedback")
    st.write(feedback)

    metrics = extract_metrics(resume_text)
    job_text = ""
    match_result = None

    job_text = st.text_area("Paste Job Description")
    if job_text:
        match_result = match_resume_to_job(resume_text, job_text)
        st.subheader("Job Match Results")
        st.write(f"Match Score: {match_result['Match Score']}")
        st.write("Missing Keywords:", match_result["Missing Keywords"])

    df = to_dataframe(metrics, feedback, match_result)
    st.subheader("Analytics")
    st.dataframe(df)

    if st.button("Export to CSV"):
        export_csv(df)
        st.success("Exported to data/reviews.csv")
    
    # df = pd.concat([existing_df, to_dataframe(metrics, feedback, match_result, version="v2")])
    # plot_match_score_trend(df)
    # plot_missing_keyword_frequency(df)   