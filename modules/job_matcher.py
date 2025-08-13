def match_resume_to_job(resume_text, job_text):
    keywords = job_text.lower().split()
    resume_words = resume_text.lower().split()
    match_score = sum([resume_words.count(k) for k in keywords])
    return {
        "Match Score": match_score,
        "Missing Keywords": [k for k in keywords if k not in resume_words]
    }