# ATS_PROMPT = """
# You are an ATS Expert.

# Analyze the Resume and Job Description.

# Return:

# 1. ATS Score (/100)
# 2. Match Percentage
# 3. Resume Summary
# 4. Skills Found
# 5. Missing Skills
# 6. Strengths
# 7. Weaknesses
# 8. Improvement Suggestions
# 9. Final Recommendation

# Resume:
# {resume}

# Job Description:
# {jd}
# """


# SKILL_GAP_PROMPT = """
# Compare Resume and JD.

# Return:

# 1. Existing Skills
# 2. Matching Skills
# 3. Missing Skills
# 4. Skill Gap Percentage

# Resume:
# {resume}

# JD:
# {jd}
# """


# INTERVIEW_PROMPT = """
# Generate interview questions based on:

# Resume:
# {resume}

# JD:
# {jd}

# Generate:

# 1. Technical Questions
# 2. Project Questions
# 3. HR Questions
# 4. Behavioral Questions
# """


# ROADMAP_PROMPT = """
# Based on Resume and JD:

# Generate:

# 1. Missing Skills
# 2. Certifications
# 3. Courses
# 4. Projects
# 5. 30-60-90 Day Roadmap

# Resume:
# {resume}

# JD:
# {jd}
# """


# COVER_LETTER_PROMPT = """
# Generate a professional cover letter.

# Resume:
# {resume}

# Job Description:
# {jd}
# """

# RESUME_REWRITE_PROMPT = """
# Rewrite and improve the resume.

# Improve:

# 1. Professional Summary
# 2. Project Descriptions
# 3. Experience Points
# 4. ATS Keywords

# Resume:

# {resume}
# """


# ai/prompt_templates.py
from pydantic import BaseModel, Field
from typing import List

# ==========================================
# 🧱 PHASE 1: PYDANTIC SCHEMA DEFINITIONS
# ==========================================

class ATSReportSchema(BaseModel):
    ats_score: int = Field(..., description="Overall score out of 100 based on structural alignment with the JD.")
    match_percentage: int = Field(..., description="Calculated functional domain percentage match.")
    resume_summary: str = Field(..., description="A crisp, metric-driven 3-sentence summary of the profile context.")
    skills_found: List[str] = Field(..., description="Core tools, technologies, and framework protocols identified.")
    missing_skills: List[str] = Field(..., description="Critical required technologies completely absent or weak in the resume.")
    strengths: List[str] = Field(..., description="Top 3 structural alignment high points.")
    weaknesses: List[str] = Field(..., description="Key professional areas lacking validation or depth.")
    improvement_suggestions: List[str] = Field(..., description="Actionable things to add or optimize.")
    final_recommendation: str = Field(..., description="Hiring decision recommendation: Strongly Match, Conditional Match, or Disconnect.")


class SkillGapSchema(BaseModel):
    existing_skills: List[str] = Field(..., description="All identifiable skills listed on the candidate profile.")
    matching_skills: List[str] = Field(..., description="Skills from the candidate profile that explicitly fulfill JD requirements.")
    missing_skills: List[str] = Field(..., description="Core skills explicitly demanded by the JD that are not found.")
    skill_gap_percentage: int = Field(..., description="Calculated deficiency percentage from 0 to 100 (high value = massive mismatch).")


class InterviewPrepSchema(BaseModel):
    technical_questions: List[str] = Field(..., description="4 deep technical core questions targeting listed and missing tools.")
    project_questions: List[str] = Field(..., description="2 architectural overview questions probing the stated projects.")
    hr_questions: List[str] = Field(..., description="2 corporate cultural/organizational value questions.")
    behavioral_questions: List[str] = Field(..., description="2 situational competency questions mapping out problem-solving skills.")


class UpskillingRoadmapSchema(BaseModel):
    missing_skills: List[str] = Field(..., description="Target skills required for structural compliance.")
    recommended_certifications: List[str] = Field(..., description="Top industry standard open-source certifications.")
    recommended_courses: List[str] = Field(..., description="Strategic theoretical concepts/courses to master.")
    mock_projects: List[str] = Field(..., description="2 practical, production-level engineering projects to construct.")
    plan_30_days: List[str] = Field(..., description="Remediation steps focusing on high-priority missing core skills.")
    plan_60_days: List[str] = Field(..., description="Building out mock project elements and verifying system tools.")
    plan_90_days: List[str] = Field(..., description="Interview prep drills and certification completions.")


class ResumeRewriteSchema(BaseModel):
    optimized_summary: str = Field(..., description="An ATS-optimized, high-impact professional candidate summary.")
    rewritten_projects: List[str] = Field(..., description="Polished descriptions of stated projects utilizing metric outcomes.")
    rewritten_experience_points: List[str] = Field(..., description="Bullet points styled using active verbs and impact matrices.")
    suggested_ats_keywords: List[str] = Field(..., description="Target keywords to weave into the text profile naturally.")


# ==========================================
# 📝 PHASE 2: SYSTEM BASE PROMPT WRAPPERS
# ==========================================

ATS_PROMPT = """
You are an advanced corporate Applicant Tracking System (ATS) optimization specialist.
Perform a strict diagnostic analysis comparing the candidate's Resume against the Target Job Description.
Be fair but rigorous. You must complete every single property inside the requested JSON output schema safely.

TARGET JOB DESCRIPTION:
{jd}

---

CANDIDATE RESUME:
{resume}
"""

SKILL_GAP_PROMPT = """
You are an expert HR Technical Data Analyst. Compare the Candidate Resume text against the targeted Job Description requirements.
Break down technical capabilities, isolate matching attributes, and pinpoint missing frameworks or tools.

TARGET JOB DESCRIPTION:
{jd}

---

CANDIDATE RESUME:
{resume}
"""

INTERVIEW_PROMPT = """
You are a Lead Technical Interviewer and Engineering Manager. 
Examine the candidate's background against the target team requirements to generate a rigorous screening interview script.

TARGET JOB DESCRIPTION:
{jd}

---

CANDIDATE RESUME:
{resume}
"""

ROADMAP_PROMPT = """
You are a Senior Corporate Career Advisor and Upskilling Coach. 
Examine the candidate's background against the target job requirements to generate an actionable upskilling roadmap to completely bridge their performance gaps.

TARGET JOB DESCRIPTION:
{jd}

---

CANDIDATE RESUME:
{resume}
"""

# Note: Cover letters are long-form prose documents and should remain standard string responses
COVER_LETTER_PROMPT = """
You are an expert Career Consultant. Write a compelling, highly professional 300-word corporate Cover Letter.
Bridge the candidate's key accomplishments directly into the corporate requirements outlined in the job description. Do not hallucinate data points.

TARGET JOB DESCRIPTION:
{jd}

---

CANDIDATE RESUME:
{resume}
"""

RESUME_REWRITE_PROMPT = """
You are an expert Resume Writer specialized in optimizing profiles for automated ATS screeners.
Rewrite the candidate's professional profile text to maximize search keyword compliance and parsing clarity. Use the structural action-verb matrix method.

CANDIDATE RESUME:
{resume}
"""