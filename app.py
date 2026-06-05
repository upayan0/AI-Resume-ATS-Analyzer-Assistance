# import streamlit as st

# from parser.resume_parser import extract_resume_text
# from parser.jd_parser import extract_jd_text

# from ai.ats_service import generate_ats_report
# from ai.interview_service import generate_interview_questions
# from ai.roadmap_service import generate_roadmap
# from ai.cover_letter_service import generate_cover_letter
# from ai.resume_rewriter_service import rewrite_resume

# st.set_page_config(
#     page_title="AI Resume ATS Analyzer",
#     layout="wide"
# )

# st.title("AI Resume ATS Analyzer")
# st.markdown("Upload Resume and Job Description")

# resume_file = st.file_uploader(
#     "Upload Resume",
#     type=["pdf"]
# )

# jd_file = st.file_uploader(
#     "Upload Job Description",
#     type=["pdf"]
# )

# if resume_file and jd_file:

#     resume_text = extract_resume_text(
#         resume_file
#     )

#     jd_text = extract_jd_text(
#         jd_file
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         if st.button("Analyze Resume"):

#             result = generate_ats_report(
#                 resume_text,
#                 jd_text
#             )

#             st.subheader("ATS Report")
#             st.write(result)

#     with col2:

#         if st.button("Interview Questions"):

#             result = generate_interview_questions(
#                 resume_text,
#                 jd_text
#             )

#             st.subheader("Interview Questions")
#             st.write(result)

#     with col3:

#         if st.button("Improvement Roadmap"):

#             result = generate_roadmap(
#                 resume_text,
#                 jd_text
#             )

#             st.subheader("Roadmap")
#             st.write(result)

#     st.divider()

#     if st.button("Rewrite Resume"):

#         result = rewrite_resume(
#             resume_text
#         )

#         st.subheader("Improved Resume")
#         st.write(result)

#     if st.button("Generate Cover Letter"):

#         result = generate_cover_letter(
#             resume_text,
#             jd_text
#         )

#         st.subheader("Cover Letter")
#         st.write(result)



# # app.py
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import os
# import sqlite3
# from datetime import datetime

# # Import document parsing utilities
# from parser.resume_parser import extract_resume_text
# from parser.jd_parser import extract_jd_text

# # Import structured Pydantic schema-driven AI microservices
# from ai.ats_service import generate_ats_report
# from ai.interview_service import generate_interview_questions
# from ai.roadmap_service import generate_roadmap
# from ai.cover_letter_service import generate_cover_letter
# from ai.resume_rewriter_service import rewrite_resume

# # Import semantic vector data operations
# from rag.faiss_store import add_document
# from rag.retrieval import retrieve_context

# # Import automated document compiler libraries
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib import colors

# # ==========================================
# # 💾 SYSTEM LAYER & STAGE SETUP INITIALIZATIONS
# # ==========================================
# DB_PATH = "database/ats_records.db"
# os.makedirs("database", exist_ok=True)
# os.makedirs("rag", exist_ok=True)
# os.makedirs("outputs", exist_ok=True)

# def init_sqlite_db():
#     with sqlite3.connect(DB_PATH) as conn:
#         conn.execute("""
#             CREATE TABLE IF NOT EXISTS CANDIDATE_ANALYSIS (
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 NAME TEXT NOT NULL,
#                 ATS_SCORE INTEGER NOT NULL,
#                 MATCH_PERCENTAGE INTEGER NOT NULL,
#                 ANALYSIS_DATE TEXT NOT NULL
#             );
#         """)
#         conn.commit()

# init_sqlite_db()

# # ==========================================
# # 🖨️ REPORT GENERATOR COMPILER (ReportLab)
# # ==========================================
# def export_pdf_report(filename: str, r: dict, path_out: str):
#     doc = SimpleDocTemplate(path_out, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
#     story = []
#     styles = getSampleStyleSheet()
    
#     t_style = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=22, spaceAfter=15, textColor=colors.HexColor("#1A365D"))
#     s_style = ParagraphStyle('S', fontName='Helvetica-Bold', fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#2B6CB0"))
#     b_style = ParagraphStyle('B', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=4)
    
#     story.append(Paragraph("Gemini AI Resume ATS Audit Assessment", t_style))
#     story.append(Spacer(1, 10))
    
#     # Structural metric breakdown matrix grid rows
#     grid = [
#         [Paragraph("<b>Evaluation Metric Category</b>", b_style), Paragraph("<b>Assigned Rating Value</b>", b_style)],
#         [Paragraph("Overall ATS Score Profile", b_style), Paragraph(f"{r.get('ats_score', 0)} / 100", b_style)],
#         [Paragraph("Functional Domain Match Weight", b_style), Paragraph(f"{r.get('match_percentage', 0)} %", b_style)],
#         [Paragraph("Hiring Status Recommendation", b_style), Paragraph(r.get('final_recommendation', 'N/A'), b_style)]
#     ]
#     t = Table(grid, colWidths=[280, 220])
#     t.setStyle(TableStyle([
#         ('BACKGROUND', (0,0), (1,0), colors.HexColor("#E2E8F0")),
#         ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
#         ('PADDING', (0,0), (-1,-1), 8),
#     ]))
#     story.append(t)
    
#     story.append(Paragraph("Executive Candidate Background Summary", s_style))
#     story.append(Paragraph(r.get('resume_summary', ''), b_style))
    
#     story.append(Paragraph("Identified Capabilities & System Strengths", s_style))
#     for strg in r.get('strengths', []):
#         story.append(Paragraph(f"• {strg}", b_style))
        
#     story.append(Paragraph("Identified Gaps & Profile Weaknesses", s_style))
#     for weak in r.get('weaknesses', []):
#         story.append(Paragraph(f"• {weak}", b_style))
        
#     doc.build(story)

# # ==========================================
# # 🎨 STREAMLIT DASHBOARD CONFIGURATION
# # ==========================================
# st.set_page_config(page_title="AI Resume ATS Analyzer", layout="wide")
# st.title("💼 AI Resume ATS Analyzer & Placement Hub")
# st.markdown("Advanced Multi-Tiered Evaluation driven by Gemini 2.5 Flash & Semantic Vector RAG Indexing")
# st.write("---")

# # Setup clean separation of duties via native structural workspace navigation layouts
# navigation_tab = st.sidebar.selectbox("Application Interface View", ["Diagnostic Assessment Suite", "Institutional Analytics Logs"])

# if navigation_tab == "Diagnostic Assessment Suite":
#     col_input, col_output = st.columns([2, 3], gap="large")
    
#     with col_input:
#         st.subheader("📋 Document Ingestion Workspace")
#         resume_file = st.file_uploader("Upload Profile Resume (PDF Only)", type=["pdf"], key="res_upload")
#         # jd_file = st.file_uploader("Upload Target Corporate Job Requirements (PDF Only)", type=["pdf"], key=\"jd_upload\")
#         jd_file = st.file_uploader("Upload Target Corporate Job Requirements (PDF Only)", type=["pdf"], key="jd_upload")
        
#         if resume_file and jd_file:
#             st.success("Documents staged successfully for analytical diagnostic processing pipeline.")
            
#             # Extract underlying raw document textual properties
#             resume_text = extract_resume_text(resume_file)
#             jd_text = extract_jd_text(jd_file)
            
#             st.write("---")
#             st.subheader("⚙️ Analysis Pipeline Triggers")
            
#             # Action button matrix blocks split tracking options explicitly
#             trigger_ats = st.button("Run Profile Compliance Diagnostics", use_container_width=True, type="primary")
#             trigger_interview = st.button("Extract Custom Interview Question Pool", use_container_width=True)
#             trigger_roadmap = st.button("Formulate Timeline Upskilling Roadmap", use_container_width=True)
#             trigger_rewrite = st.button("Generate ATS Friendly Resume Rewrite", use_container_width=True)
#             trigger_cover = st.button("Draft Tailored Corporate Cover Letter", use_container_width=True)
            
#     with col_output:
#         st.subheader("📊 Dynamic Diagnostic Insights")
        
#         if resume_file and jd_file:
#             # --- RAG Index Pipeline Phase ---
#             # Automatically parse and vector-index text fragments locally into FAISS to preserve contextual semantic bounds
#             from rag.embeddings import generate_embedding
#             emb = generate_embedding(resume_text)
#             add_document(doc_id=resume_file.name, text=resume_text, embedding=emb)
            
#             # Isolate semantic context using RAG index before hitting core generation layers
#             rag_context_resume = retrieve_context(jd_text, top_k=3)
            
#             if trigger_ats:
#                 with st.spinner("Calculating matching metrics parameters..."):
#                     # Execute schema-driven service loop
#                     report = generate_ats_report(rag_context_resume, jd_text)
#                     st.session_state["active_report"] = report
                    
#                     # 📈 Render Gauge Visualizations with Plotly
#                     fig_gauge = go.Figure(go.Indicator(
#                         mode="gauge+number",
#                         value=report.get("ats_score", 0),
#                         title={'text': "Calculated ATS Score"},
#                         gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2B6CB0"}}
#                     ))
#                     st.plotly_chart(fig_gauge, use_container_width=True)
                    
#                     # Persist tracking history data rows securely within relational SQLite database
#                     with sqlite3.connect(DB_PATH) as conn:
#                         conn.execute("""
#                             INSERT INTO CANDIDATE_ANALYSIS (NAME, ATS_SCORE, MATCH_PERCENTAGE, ANALYSIS_DATE)
#                             VALUES (?, ?, ?, ?);
#                         """, (resume_file.name, report.get("ats_score", 0), report.get("match_percentage", 0), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
#                         conn.commit()
                        
#                     # Presentation dashboard fields
#                     st.success(f"### Score Alignment: **{report.get('ats_score')}/100**")
#                     st.info(f"**Functional Skill Match Matrix Balance:** {report.get('match_percentage')}%")
#                     st.markdown(f"**Executive Profile Summary:** {report.get('resume_summary')}")
                    
#                     col_str, col_weak = st.columns(2)
#                     with col_str:
#                         st.markdown("🎯 **Core Background Strengths:**")
#                         for item in report.get("strengths", []):
#                             st.markdown(f"- {item}")
#                     with col_weak:
#                         st.markdown("⚠️ **Identified Structural Gaps:**")
#                         for item in report.get("weaknesses", []):
#                             st.markdown(f"- {item}")
                            
#             elif trigger_interview:
#                 with st.spinner("Formulating customized interview evaluation parameters..."):
#                     interview_data = generate_interview_questions(rag_context_resume, jd_text)
                    
#                     for cat, key in [("Technical Drills", "technical_questions"), ("Project Architectural Review", "project_questions"), ("HR Cultural Screening", "hr_questions"), ("Behavioral Scenarios", "behavioral_questions")]:
#                         with st.expander(f"🎙️ View Tailored {cat}"):
#                             for q in interview_data.get(key, []):
#                                 st.markdown(f"* {q}")
                                
#             elif trigger_roadmap:
#                 with st.spinner("Drafting strategic training track blueprints..."):
#                     roadmap_data = generate_roadmap(rag_context_resume, jd_text)
                    
#                     st.markdown("### 🛠️ Personal Upskilling Curated Blueprint")
#                     st.write(f"**Missing Core Domain Skills:** {', '.join(roadmap_data.get('missing_skills', []))}")
#                     st.write(f"**Target Open-Source Credentials:** {', '.join(roadmap_data.get('recommended_certifications', []))}")
                    
#                     tab_m1, tab_m2, tab_m3 = st.tabs(["📅 Days 1-30", "📅 Days 31-60", "📅 Days 61-90"])
#                     with tab_m1:
#                         for steps in roadmap_data.get("plan_30_days", []): st.markdown(f"- {steps}")
#                     with tab_m2:
#                         for steps in roadmap_data.get("plan_60_days", []): st.markdown(f"- {steps}")
#                     with tab_m3:
#                         for steps in roadmap_data.get("plan_90_days", []): st.markdown(f"- {steps}")
                        
#             elif trigger_rewrite:
#                 with st.spinner("Refactoring project bullet structures..."):
#                     rewrite_data = rewrite_resume(rag_context_resume)
#                     st.markdown("### ✍️ Professional Experience Structural Adjustments")
#                     st.markdown(f"**Optimized Stated Summary:**\n_{rewrite_data.get('optimized_summary')}_")
                    
#                     with st.expander("📝 View Optimized Stated Projects & Achievements Bullet Adjustments"):
#                         for bp in rewrite_data.get("rewritten_projects", []): st.markdown(f"* {bp}")
#                     st.caption(f"**Target System Keywords To Inject:** {', '.join(rewrite_data.get('suggested_ats_keywords', []))}")
                    
#             elif trigger_cover:
#                 with st.spinner("Drafting professional persuasive business text letter..."):
#                     cover_letter_prose = generate_cover_letter(rag_context_resume, jd_text)
#                     st.markdown("### 📝 Tailored Professional Business Letter")
#                     st.text_area("Prose Copy Container Box", value=cover_letter_prose, height=350)
                    
#             # PDF Generation Layer Download Action Button Hook
#             if "active_report" in st.session_state:
#                 st.write("---")
#                 pdf_filename = f"{resume_file.name}_Verification_Audit.pdf"
#                 pdf_filepath = f"outputs/{pdf_filename}"
                
#                 if st.button("Compile Downloadable PDF Compliance Verification Report"):
#                     export_pdf_report(pdf_filename, st.session_state["active_report"], pdf_filepath)
#                     with open(pdf_filepath, "rb") as f_stream:
#                         st.download_button("Click here to save PDF document", f_stream, file_name=pdf_filename)
#         else:
#             st.info("Awaiting file drops. Upload matching PDF profiles inside the configuration panel to unlock optimization panels.")

# # ==========================================
# # 📜 WORKSPACE SUITE 2: INSTITUTIONAL ANALYTICS LOGS
# # ==========================================
# elif navigation_tab == "Institutional Analytics Logs":
#     st.subheader("📜 System Historic Compliance Audits Database Records")
    
#     with sqlite3.connect(DB_PATH) as connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT NAME, ATS_SCORE, MATCH_PERCENTAGE, ANALYSIS_DATE FROM CANDIDATE_ANALYSIS ORDER BY ID DESC;")
#         log_rows = cursor.fetchall()
        
#     if log_rows:
#         df_logs = pd.DataFrame(log_rows, columns=["Candidate Staged File Name", "ATS Diagnostic Score", "Domain Skill Match Weight %", "Analysis Generation Timestamp"])
        
#         # Display high-level campus placement distributions metrics
#         col_m1, col_m2 = st.columns(2)
#         with col_m1:
#             st.metric("Total Corporate Profile Appraisals Executed", len(df_logs))
#         with col_m2:
#             st.metric("Mean System Selection Matching Metric Score", f"{round(df_logs['ATS Diagnostic Score'].mean(), 1)} / 100")
            
#         st.write("---")
#         st.dataframe(df_logs, use_container_width=True)
#     else:
#         st.info("Tracking database contains zero processed candidate logs at this operational checkpoint.")






# # app.py
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import os
# import sqlite3
# from datetime import datetime

# # Import document parsing utilities
# from parser.resume_parser import extract_resume_text
# from parser.jd_parser import extract_jd_text

# # Import structured Pydantic schema-driven AI microservices
# from ai.ats_service import generate_ats_report
# from ai.interview_service import generate_interview_questions
# from ai.roadmap_service import generate_roadmap
# from ai.cover_letter_service import generate_cover_letter
# from ai.resume_rewriter_service import rewrite_resume

# # Import semantic vector data operations
# from rag.faiss_store import add_document
# from rag.retrieval import retrieve_context

# # Import automated document compiler libraries
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib import colors

# # ==========================================
# # 💾 SYSTEM LAYER & STAGE SETUP INITIALIZATIONS
# # ==========================================
# DB_PATH = "database/ats_records.db"
# os.makedirs("database", exist_ok=True)
# os.makedirs("rag", exist_ok=True)
# os.makedirs("outputs", exist_ok=True)

# def init_sqlite_db():
#     with sqlite3.connect(DB_PATH) as conn:
#         conn.execute("""
#             CREATE TABLE IF NOT EXISTS CANDIDATE_ANALYSIS (
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 NAME TEXT NOT NULL,
#                 ATS_SCORE INTEGER NOT NULL,
#                 MATCH_PERCENTAGE INTEGER NOT NULL,
#                 ANALYSIS_DATE TEXT NOT NULL
#             );
#         """)
#         conn.commit()

# init_sqlite_db()

# # ==========================================
# # 🖨️ REPORT GENERATOR COMPILER (ReportLab)
# # ==========================================
# def export_pdf_report(filename: str, r: dict, path_out: str):
#     doc = SimpleDocTemplate(path_out, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
#     story = []
#     styles = getSampleStyleSheet()
    
#     t_style = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=22, spaceAfter=15, textColor=colors.HexColor("#1A365D"))
#     s_style = ParagraphStyle('S', fontName='Helvetica-Bold', fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#2B6CB0"))
#     b_style = ParagraphStyle('B', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=4)
    
#     story.append(Paragraph("Gemini AI Resume ATS Audit Assessment", t_style))
#     story.append(Spacer(1, 10))
    
#     grid = [
#         [Paragraph("<b>Evaluation Metric Category</b>", b_style), Paragraph("<b>Assigned Rating Value</b>", b_style)],
#         [Paragraph("Overall ATS Score Profile", b_style), Paragraph(f"{r.get('ats_score', 0)} / 100", b_style)],
#         [Paragraph("Functional Domain Match Weight", b_style), Paragraph(f"{r.get('match_percentage', 0)} %", b_style)],
#         [Paragraph("Hiring Status Recommendation", b_style), Paragraph(r.get('final_recommendation', 'N/A'), b_style)]
#     ]
#     t = Table(grid, colWidths=[280, 220])
#     t.setStyle(TableStyle([
#         ('BACKGROUND', (0,0), (1,0), colors.HexColor("#E2E8F0")),
#         ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
#         ('PADDING', (0,0), (-1,-1), 8),
#     ]))
#     story.append(t)
    
#     story.append(Paragraph("Executive Candidate Background Summary", s_style))
#     story.append(Paragraph(r.get('resume_summary', ''), b_style))
    
#     story.append(Paragraph("Identified Capabilities & System Strengths", s_style))
#     for strg in r.get('strengths', []):
#         story.append(Paragraph(f"• {strg}", b_style))
        
#     story.append(Paragraph("Identified Gaps & Profile Weaknesses", s_style))
#     for weak in r.get('weaknesses', []):
#         story.append(Paragraph(f"• {weak}", b_style))
        
#     doc.build(story)

# # ==========================================
# # 🎨 STREAMLIT DASHBOARD CONFIGURATION
# # ==========================================
# st.set_page_config(page_title="AI Resume ATS Analyzer", layout="wide")
# st.title("💼 AI Resume ATS Analyzer & Placement Hub")
# st.markdown("Advanced Multi-Tiered Evaluation driven by Gemini 2.5 Flash & Semantic Vector RAG Indexing")
# st.write("---")

# navigation_tab = st.sidebar.selectbox("Application Interface View", ["Diagnostic Assessment Suite", "Institutional Analytics Logs"])

# if navigation_tab == "Diagnostic Assessment Suite":
#     col_input, col_output = st.columns([2, 3], gap="large")
    
#     with col_input:
#         st.subheader("📋 Document Ingestion Workspace")
#         resume_file = st.file_uploader("Upload Profile Resume (PDF Only)", type=["pdf"], key="res_upload")
        
#         st.write("---")
#         # 🆕 Dynamic Selector for choosing the JD ingestion style
#         jd_input_mode = st.radio(
#             "Select Job Description Input Method:",
#             ["Upload PDF File", "Paste Raw Text Specification"],
#             horizontal=True,
#             key="jd_mode_selector"
#         )
        
#         # Operational variables to securely manage downstream layout matching
#         jd_text = ""
#         jd_staged = False
        
#         # Branch the input UI layout conditionally based on selection
#         if jd_input_mode == "Upload PDF File":
#             jd_file = st.file_uploader("Upload Target Corporate Job Requirements (PDF Only)", type=["pdf"], key="jd_upload")
#             if resume_file and jd_file:
#                 jd_text = extract_jd_text(jd_file)
#                 jd_staged = True
#         else:
#             jd_text_area = st.text_area(
#                 "Paste Corporate Job Requirements / Evaluation Guidelines",
#                 height=250,
#                 placeholder="Paste the core corporate specifications, technical stacks, and experience guidelines here...",
#                 key="jd_text_pure"
#             )
#             if resume_file and jd_text_area.strip():
#                 jd_text = jd_text_area.strip()
#                 jd_staged = True
        
#         # Unlocks the analysis option matrix once both configurations are set
#         if resume_file and jd_staged:
#             st.success("Documents staged successfully for analytical diagnostic processing pipeline.")
            
#             # Extract underlying raw document textual properties
#             resume_text = extract_resume_text(resume_file)
            
#             st.write("---")
#             st.subheader("⚙️ Analysis Pipeline Triggers")
            
#             # Action button matrix blocks split tracking options explicitly
#             trigger_ats = st.button("Run Profile Compliance Diagnostics", use_container_width=True, type="primary")
#             trigger_interview = st.button("Extract Custom Interview Question Pool", use_container_width=True)
#             trigger_roadmap = st.button("Formulate Timeline Upskilling Roadmap", use_container_width=True)
#             trigger_rewrite = st.button("Generate ATS Friendly Resume Rewrite", use_container_width=True)
#             trigger_cover = st.button("Draft Tailored Corporate Cover Letter", use_container_width=True)
            
#     with col_output:
#         st.subheader("📊 Dynamic Diagnostic Insights")
        
#         if resume_file and jd_staged:
#             # --- RAG Index Pipeline Phase ---
#             # Automatically parse and vector-index text fragments locally into FAISS to preserve contextual semantic bounds
#             from rag.embeddings import generate_embedding
#             emb = generate_embedding(resume_text)
#             add_document(doc_id=resume_file.name, text=resume_text, embedding=emb)
            
#             # Isolate semantic context using RAG index before hitting core generation layers
#             rag_context_resume = retrieve_context(jd_text, top_k=3)
            
#             if trigger_ats:
#                 with st.spinner("Calculating matching metrics parameters..."):
#                     # Execute schema-driven service loop
#                     report = generate_ats_report(rag_context_resume, jd_text)
#                     st.session_state["active_report"] = report
                    
#                     # 📈 Render Gauge Visualizations with Plotly
#                     fig_gauge = go.Figure(go.Indicator(
#                         mode="gauge+number",
#                         value=report.get("ats_score", 0),
#                         title={'text': "Calculated ATS Score"},
#                         gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2B6CB0"}}
#                     ))
#                     st.plotly_chart(fig_gauge, use_container_width=True)
                    
#                     # Persist tracking history data rows securely within relational SQLite database
#                     with sqlite3.connect(DB_PATH) as conn:
#                         conn.execute("""
#                             INSERT INTO CANDIDATE_ANALYSIS (NAME, ATS_SCORE, MATCH_PERCENTAGE, ANALYSIS_DATE)
#                             VALUES (?, ?, ?, ?);
#                         """, (resume_file.name, report.get("ats_score", 0), report.get("match_percentage", 0), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
#                         conn.commit()
                        
#                     # Presentation dashboard fields
#                     st.success(f"### Score Alignment: **{report.get('ats_score')}/100**")
#                     st.info(f"**Functional Skill Match Matrix Balance:** {report.get('match_percentage')}%")
#                     st.markdown(f"**Executive Profile Summary:** {report.get('resume_summary')}")
                    
#                     col_str, col_weak = st.columns(2)
#                     with col_str:
#                         st.markdown("🎯 **Core Background Strengths:**")
#                         for item in report.get("strengths", []):
#                             st.markdown(f"- {item}")
#                     with col_weak:
#                         st.markdown("⚠️ **Identified Structural Gaps:**")
#                         for item in report.get("weaknesses", []):
#                             st.markdown(f"- {item}")
                            
#             elif trigger_interview:
#                 with st.spinner("Formulating customized interview evaluation parameters..."):
#                     interview_data = generate_interview_questions(rag_context_resume, jd_text)
                    
#                     for cat, key in [("Technical Drills", "technical_questions"), ("Project Architectural Review", "project_questions"), ("HR Cultural Screening", "hr_questions"), ("Behavioral Scenarios", "behavioral_questions")]:
#                         with st.expander(f"🎙️ View Tailored {cat}"):
#                             for q in interview_data.get(key, []):
#                                 st.markdown(f"* {q}")
                                
#             elif trigger_roadmap:
#                 with st.spinner("Drafting strategic training track blueprints..."):
#                     roadmap_data = generate_roadmap(rag_context_resume, jd_text)
                    
#                     st.markdown("### 🛠️ Personal Upskilling Curated Blueprint")
#                     st.write(f"**Missing Core Domain Skills:** {', '.join(roadmap_data.get('missing_skills', []))}")
#                     st.write(f"**Target Open-Source Credentials:** {', '.join(roadmap_data.get('recommended_certifications', []))}")
                    
#                     tab_m1, tab_m2, tab_m3 = st.tabs(["📅 Days 1-30", "📅 Days 31-60", "📅 Days 61-90"])
#                     with tab_m1:
#                         for steps in roadmap_data.get("plan_30_days", []): st.markdown(f"- {steps}")
#                     with tab_m2:
#                         for steps in roadmap_data.get("plan_60_days", []): st.markdown(f"- {steps}")
#                     with tab_m3:
#                         for steps in roadmap_data.get("plan_90_days", []): st.markdown(f"- {steps}")
                        
#             elif trigger_rewrite:
#                 with st.spinner("Refactoring project bullet structures..."):
#                     rewrite_data = rewrite_resume(rag_context_resume)
#                     st.markdown("### ✍️ Professional Experience Structural Adjustments")
#                     st.markdown(f"**Optimized Stated Summary:**\n_{rewrite_data.get('optimized_summary')}_")
                    
#                     with st.expander("📝 View Optimized Stated Projects & Achievements Bullet Adjustments"):
#                         for bp in rewrite_data.get("rewritten_projects", []): st.markdown(f"* {bp}")
#                     st.caption(f"**Target System Keywords To Inject:** {', '.join(rewrite_data.get('suggested_ats_keywords', []))}")
                    
#             elif trigger_cover:
#                 with st.spinner("Drafting professional persuasive business text letter..."):
#                     cover_letter_prose = generate_cover_letter(rag_context_resume, jd_text)
#                     st.markdown("### 📝 Tailored Professional Business Letter")
#                     st.text_area("Prose Copy Container Box", value=cover_letter_prose, height=350)
                    
#             # PDF Generation Layer Download Action Button Hook
#             if "active_report" in st.session_state:
#                 st.write("---")
#                 pdf_filename = f"{resume_file.name}_Verification_Audit.pdf"
#                 pdf_filepath = f"outputs/{pdf_filename}"
                
#                 if st.button("Compile Downloadable PDF Compliance Verification Report"):
#                     export_pdf_report(pdf_filename, st.session_state["active_report"], pdf_filepath)
#                     with open(pdf_filepath, "rb") as f_stream:
#                         st.download_button("Click here to save PDF document", f_stream, file_name=pdf_filename)
#         else:
#             st.info("Awaiting file drops. Upload matching PDF profiles or paste description elements inside the layout panel to unlock calculations.")

# # ==========================================
# # 📜 WORKSPACE SUITE 2: INSTITUTIONAL ANALYTICS LOGS
# # ==========================================
# elif navigation_tab == "Institutional Analytics Logs":
#     st.subheader("📜 System Historic Compliance Audits Database Records")
    
#     with sqlite3.connect(DB_PATH) as connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT NAME, ATS_SCORE, MATCH_PERCENTAGE, ANALYSIS_DATE FROM CANDIDATE_ANALYSIS ORDER BY ID DESC;")
#         log_rows = cursor.fetchall()
        
#     if log_rows:
#         df_logs = pd.DataFrame(log_rows, columns=["Candidate Staged File Name", "ATS Diagnostic Score", "Domain Skill Match Weight %", "Analysis Generation Timestamp"])
        
#         col_m1, col_m2 = st.columns(2)
#         with col_m1:
#             st.metric("Total Corporate Profile Appraisals Executed", len(df_logs))
#         with col_m2:
#             st.metric("Mean System Selection Matching Metric Score", f"{round(df_logs['ATS Diagnostic Score'].mean(), 1)} / 100")
            
#         st.write("---")
#         st.dataframe(df_logs, use_container_width=True)
#     else:
#         st.info("Tracking database contains zero processed candidate logs at this operational checkpoint.")




# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import sqlite3
from datetime import datetime

# Import document parsing utilities
from parser.resume_parser import extract_resume_text
from parser.jd_parser import extract_jd_text

# Import structured Pydantic schema-driven AI microservices
from ai.ats_service import generate_ats_report
from ai.interview_service import generate_interview_questions
from ai.roadmap_service import generate_roadmap
from ai.cover_letter_service import generate_cover_letter
from ai.resume_rewriter_service import rewrite_resume

# Import semantic vector data operations
from rag.faiss_store import add_document
from rag.retrieval import retrieve_context

# Import automated document compiler libraries
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ==========================================
# 💾 SYSTEM LAYER & STAGE SETUP INITIALIZATIONS
# ==========================================
DB_PATH = "database/ats_records.db"
os.makedirs("database", exist_ok=True)
os.makedirs("rag", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

def init_sqlite_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS CANDIDATE_ANALYSIS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT NOT NULL,
                ATS_SCORE INTEGER NOT NULL,
                MATCH_PERCENTAGE INTEGER NOT NULL,
                ANALYSIS_DATE TEXT NOT NULL
            );
        """)
        conn.commit()

init_sqlite_db()

# ==========================================
# 🖨️ REPORT GENERATOR COMPILERS (ReportLab)
# ==========================================
def export_pdf_report(filename: str, r: dict, path_out: str):
    """Compiles the structural compliance evaluation report."""
    doc = SimpleDocTemplate(path_out, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()
    
    t_style = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=22, spaceAfter=15, textColor=colors.HexColor("#1A365D"))
    s_style = ParagraphStyle('S', fontName='Helvetica-Bold', fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#2B6CB0"))
    b_style = ParagraphStyle('B', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=4)
    
    story.append(Paragraph("Gemini AI Resume ATS Audit Assessment", t_style))
    story.append(Spacer(1, 10))
    
    grid = [
        [Paragraph("<b>Evaluation Metric Category</b>", b_style), Paragraph("<b>Assigned Rating Value</b>", b_style)],
        [Paragraph("Overall ATS Score Profile", b_style), Paragraph(f"{r.get('ats_score', 0)} / 100", b_style)],
        [Paragraph("Functional Domain Match Weight", b_style), Paragraph(f"{r.get('match_percentage', 0)} %", b_style)],
        [Paragraph("Hiring Status Recommendation", b_style), Paragraph(r.get('final_recommendation', 'N/A'), b_style)]
    ]
    t = Table(grid, colWidths=[280, 220])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), colors.HexColor("#E2E8F0")),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t)
    
    story.append(Paragraph("Executive Candidate Background Summary", s_style))
    story.append(Paragraph(r.get('resume_summary', ''), b_style))
    
    story.append(Paragraph("Identified Capabilities & System Strengths", s_style))
    for strg in r.get('strengths', []):
        story.append(Paragraph(f"• {strg}", b_style))
        
    story.append(Paragraph("Identified Gaps & Profile Weaknesses", s_style))
    for weak in r.get('weaknesses', []):
        story.append(Paragraph(f"• {weak}", b_style))
        
    doc.build(story)


def export_rewritten_resume_pdf(filename: str, r: dict, path_out: str):
    """
    Compiles the structured AI-rewritten components into an authentic, 
    industry-standard corporate resume template format.
    """
    # Set standard tight corporate margins (0.5 inch / 36 points) to maximize text layout on a single page
    doc = SimpleDocTemplate(path_out, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story = []
    styles = getSampleStyleSheet()
    
    # 🎨 Executive Typographical Palette
    primary_color = colors.HexColor("#0F172A")    # Deep Slate / Charcoal Header
    secondary_color = colors.HexColor("#1E3A8A")  # Corporate Royal Blue Section Titles
    text_color = colors.HexColor("#334155")       # Muted Charcoal Body Text

    name_style = ParagraphStyle('ResName', fontName='Helvetica-Bold', fontSize=22, leading=26, alignment=1, spaceAfter=2, textColor=primary_color)
    contact_style = ParagraphStyle('ResContact', fontName='Helvetica', fontSize=9, leading=12, alignment=1, spaceAfter=12, textColor=text_color)
    section_title_style = ParagraphStyle('ResSecTitle', fontName='Helvetica-Bold', fontSize=12, leading=14, spaceBefore=8, spaceAfter=4, textColor=secondary_color)
    body_style = ParagraphStyle('ResBody', fontName='Helvetica', fontSize=9.5, leading=14, spaceAfter=6, textColor=colors.HexColor("#1E293B"))
    bullet_style = ParagraphStyle('ResBullet', fontName='Helvetica', fontSize=9, leading=13.5, leftIndent=12, firstLineIndent=-8, spaceAfter=3, textColor=colors.HexColor("#334155"))
    keyword_title_style = ParagraphStyle('ResKeyTitle', fontName='Helvetica-Bold', fontSize=9, leading=13, textColor=colors.HexColor("#1E293B"))

    # =====================================================================
    # 1. PERSONAL HEADER & CONTACT DETAILS
    # =====================================================================
    story.append(Paragraph("UPAYAN CHATTERJEE", name_style))
    story.append(Paragraph("Kolkata, West Bengal, India | +91 6291581144 | github.com/UpayanChatterjee | linkedin.com/in/upayan-chatterjee", contact_style))
    
    def draw_section_divider(title_text):
        """Creates a professional section title with a clean running rule beneath it."""
        elements = [
            Paragraph(title_text, section_title_style),
            Spacer(1, 1)
        ]
        # Use a slim 1-row table as a horizontal aesthetic accent rule
        rule_table = Table([[""]], colWidths=[540], rowHeights=[1])
        rule_table.setStyle(TableStyle([
            ('LINEABOVE', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        elements.append(rule_table)
        elements.append(Spacer(1, 4))
        return elements

    # =====================================================================
    # 2. PROFESSIONAL SUMMARY
    # =====================================================================
    story.extend(draw_section_divider("PROFESSIONAL SUMMARY"))
    story.append(Paragraph(r.get('optimized_summary', 'Results-driven computer science engineering student focusing on enterprise full-stack software development and robust automated data system parsing execution loop tracking pipelines.'), body_style))
    story.append(Spacer(1, 4))

    # =====================================================================
    # 3. CORE TECHNICAL SKILLS MATRIX
    # =====================================================================
    story.extend(draw_section_divider("TECHNICAL COMPETENCIES"))
    
    # Isolate system keywords dynamically into categorization strings
    all_keywords = r.get('suggested_ats_keywords', [])
    
    # Smart structural grouping text categories fallbacks 
    langs = [k for k in all_keywords if k.lower() in ['java', 'python', 'sql', 'c++', 'javascript']] or ['Java', 'SQL', 'Python', 'C++']
    frames = [k for k in all_keywords if k.lower() in ['spring boot', 'mvc', 'hibernate', 'pydantic', 'streamlit']] or ['Spring Boot', 'Spring MVC', 'REST APIs', 'Maven']
    tools = [k for k in all_keywords if k.lower() in ['faiss', 'sqlite', 'power bi', 'excel', 'git', 'reportlab']] or ['Microsoft Power BI', 'Advanced Excel', 'FAISS Vector Index', 'SQLite']
    
    skills_grid = [
        [Paragraph("<b>Programming Languages:</b>", keyword_title_style), Paragraph(", ".join(langs), body_style)],
        [Paragraph("<b>Frameworks & Protocols:</b>", keyword_title_style), Paragraph(", ".join(frames), body_style)],
        [Paragraph("<b>Tools & Data Engines:</b>", keyword_title_style), Paragraph(", ".join(tools), body_style)]
    ]
    
    skills_table = Table(skills_grid, colWidths=[140, 400])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # =====================================================================
    # 4. PROFESSIONAL EXPERIENCE & ACHIEVEMENTS
    # =====================================================================
    if r.get('rewritten_experience_points'):
        story.extend(draw_section_divider("PROFESSIONAL EXPERIENCE & INTERNSHIPS"))
        
        exp_header = [
            [Paragraph("<b>Software Engineering Trainee</b>", body_style), Paragraph("<b>Kolkata, WB</b>", ParagraphStyle('R', parent=body_style, alignment=2))],
            [Paragraph("<i>Technology Services Enterprise</i>", body_style), Paragraph("<i>Dec 2025 – Present</i>", ParagraphStyle('R', parent=body_style, alignment=2))]
        ]
        t_exp = Table(exp_header, colWidths=[270, 270])
        t_exp.setStyle(TableStyle([('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
        story.append(t_exp)
        story.append(Spacer(1, 2))
        
        for point in r.get('rewritten_experience_points', []):
            story.append(Paragraph(f"• {point}", bullet_style))
        story.append(Spacer(1, 4))

    # =====================================================================
    # 5. TECHNICAL SYSTEMS PROJECTS
    # =====================================================================
    story.extend(draw_section_divider("TECHNICAL PROJECTS & ARCHITECTURES"))
    
    # Project 1 Header Block
    p1_header = [
        [Paragraph("<b>Full-Stack Student Management Portal</b>", body_style), Paragraph("<i>Java, Spring Boot, MVC, Maven</i>", ParagraphStyle('R', parent=body_style, alignment=2))]
    ]
    t_p1 = Table(p1_header, colWidths=[340, 200])
    t_p1.setStyle(TableStyle([('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p1)
    story.append(Spacer(1, 2))
    
    proj_points = r.get('rewritten_projects', [])
    p1_points = [p for p in proj_points if any(w in p.lower() for w in ['student', 'portal', 'management', 'java', 'mvc', 'spring'])]
    
    if p1_points:
        for pt in p1_points[:3]:
            story.append(Paragraph(f"• {pt}", bullet_style))
    else:
        story.append(Paragraph("• Engineered an enterprise-standard full-stack management web platform deploying Spring Boot microservices routing protocols.", bullet_style))
        story.append(Paragraph("• Implemented strict MVC computational patterns to isolate client request parsing tracking parameters safely from atomic operations.", bullet_style))
    
    story.append(Spacer(1, 4))
    
    # Project 2 Header Block
    p2_header = [
        [Paragraph("<b>SafeSpace Multi-Agent AI System & Analytics Dashboard</b>", body_style), Paragraph("<i>Python, Power BI, FAISS RAG, SQLite</i>", ParagraphStyle('R', parent=body_style, alignment=2))]
    ]
    t_p2 = Table(p2_header, colWidths=[340, 200])
    t_p2.setStyle(TableStyle([('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p2)
    story.append(Spacer(1, 2))
    
    p2_points = [p for p in proj_points if p not in p1_points]
    if p2_points:
        for pt in p2_points[:3]:
            story.append(Paragraph(f"• {pt}", bullet_style))
    else:
        story.append(Paragraph("• Designed an intelligent multi-agent telemetry orchestration system leveraging local vector embeddings and semantic FAISS proximity indexing.", bullet_style))
        story.append(Paragraph("• Structured interactive relational tracking queries inside an active SQLite backend layer to surface metric data configurations safely.", bullet_style))

    # =====================================================================
    # 6. ACADEMIC CREDENTIALS
    # =====================================================================
    story.extend(draw_section_divider("EDUCATION"))
    edu_table = [
        [Paragraph("<b>B.Tech in Computer Science and Engineering (CSE)</b>", body_style), Paragraph("<b>Graduation: 2026</b>", ParagraphStyle('R', parent=body_style, alignment=2))],
        [Paragraph("Maulana Abul Kalam Azad University of Technology (MAKAUT)", body_style), Paragraph("West Bengal, India", ParagraphStyle('R', parent=body_style, alignment=2))]
    ]
    t_edu = Table(edu_table, colWidths=[380, 160])
    t_edu.setStyle(TableStyle([('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    story.append(t_edu)

    doc.build(story)

# ==========================================
# 🎨 STREAMLIT DASHBOARD CONFIGURATION
# ==========================================
st.set_page_config(page_title="AI Resume ATS Analyzer", layout="wide")
st.title("💼 AI Resume ATS Analyzer & Placement Hub")
st.markdown("Advanced Multi-Tiered Evaluation driven by Gemini 2.5 Flash & Semantic Vector RAG Indexing")
st.write("---")

navigation_tab = st.sidebar.selectbox("Application Interface View", ["Diagnostic Assessment Suite", "Institutional Analytics Logs"])

if navigation_tab == "Diagnostic Assessment Suite":
    col_input, col_output = st.columns([2, 3], gap="large")
    
    with col_input:
        st.subheader("📋 Document Ingestion Workspace")
        resume_file = st.file_uploader("Upload Profile Resume (PDF Only)", type=["pdf"], key="res_upload")
        
        st.write("---")
        # Dynamic Input Toggle Modes for Job Specification
        jd_input_mode = st.radio(
            "Select Job Description Input Method:",
            ["Upload PDF File", "Paste Raw Text Specification"],
            horizontal=True,
            key="jd_mode_selector"
        )
        
        jd_text = ""
        jd_staged = False
        
        if jd_input_mode == "Upload PDF File":
            jd_file = st.file_uploader("Upload Target Corporate Job Requirements (PDF Only)", type=["pdf"], key="jd_upload")
            if resume_file and jd_file:
                jd_text = extract_jd_text(jd_file)
                jd_staged = True
        else:
            jd_text_area = st.text_area(
                "Paste Corporate Job Requirements / Evaluation Guidelines",
                height=250,
                placeholder="Paste the core corporate specifications, technical stacks, and experience guidelines here...",
                key="jd_text_pure"
            )
            if resume_file and jd_text_area.strip():
                jd_text = jd_text_area.strip()
                jd_staged = True
        
        if resume_file and jd_staged:
            st.success("Documents staged successfully for analytical diagnostic processing pipeline.")
            resume_text = extract_resume_text(resume_file)
            
            st.write("---")
            st.subheader("⚙️ Analysis Pipeline Triggers")
            
            trigger_ats = st.button("Run Profile Compliance Diagnostics", use_container_width=True, type="primary")
            trigger_interview = st.button("Extract Custom Interview Question Pool", use_container_width=True)
            trigger_roadmap = st.button("Formulate Timeline Upskilling Roadmap", use_container_width=True)
            trigger_rewrite = st.button("Generate ATS Friendly Resume Rewrite", use_container_width=True)
            trigger_cover = st.button("Draft Tailored Corporate Cover Letter", use_container_width=True)
            
    with col_output:
        st.subheader("📊 Dynamic Diagnostic Insights")
        
        if resume_file and jd_staged:
            # --- RAG Index Pipeline Phase ---
            from rag.embeddings import generate_embedding
            emb = generate_embedding(resume_text)
            add_document(doc_id=resume_file.name, text=resume_text, embedding=emb)
            
            rag_context_resume = retrieve_context(jd_text, top_k=3)
            
            if trigger_ats:
                with st.spinner("Calculating matching metrics parameters..."):
                    report = generate_ats_report(rag_context_resume, jd_text)
                    st.session_state["active_report"] = report
                    
                    fig_gauge = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=report.get("ats_score", 0),
                        title={'text': "Calculated ATS Score"},
                        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2B6CB0"}}
                    ))
                    st.plotly_chart(fig_gauge, use_container_width=True)
                    
                    with sqlite3.connect(DB_PATH) as conn:
                        conn.execute("""
                            INSERT INTO CANDIDATE_ANALYSIS (NAME, ATS_SCORE, MATCH_PERCENTAGE, ANALYSIS_DATE)
                            VALUES (?, ?, ?, ?);
                        """, (resume_file.name, report.get("ats_score", 0), report.get("match_percentage", 0), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        conn.commit()
                        
                    st.success(f"### Score Alignment: **{report.get('ats_score')}/100**")
                    st.info(f"**Functional Skill Match Matrix Balance:** {report.get('match_percentage')}%")
                    st.markdown(f"**Executive Profile Summary:** {report.get('resume_summary')}")
                    
                    col_str, col_weak = st.columns(2)
                    with col_str:
                        st.markdown("🎯 **Core Background Strengths:**")
                        for item in report.get("strengths", []): st.markdown(f"- {item}")
                    with col_weak:
                        st.markdown("⚠️ **Identified Structural Gaps:**")
                        for item in report.get("weaknesses", []): st.markdown(f"- {item}")
                            
            elif trigger_interview:
                with st.spinner("Formulating customized interview evaluation parameters..."):
                    interview_data = generate_interview_questions(rag_context_resume, jd_text)
                    for cat, key in [("Technical Drills", "technical_questions"), ("Project Architectural Review", "project_questions"), ("HR Cultural Screening", "hr_questions"), ("Behavioral Scenarios", "behavioral_questions")]:
                        with st.expander(f"🎙️ View Tailored {cat}"):
                            for q in interview_data.get(key, []): st.markdown(f"* {q}")
                                
            elif trigger_roadmap:
                with st.spinner("Drafting strategic training track blueprints..."):
                    roadmap_data = generate_roadmap(rag_context_resume, jd_text)
                    st.markdown("### 🛠️ Personal Upskilling Curated Blueprint")
                    st.write(f"**Missing Core Domain Skills:** {', '.join(roadmap_data.get('missing_skills', []))}")
                    st.write(f"**Target Open-Source Credentials:** {', '.join(roadmap_data.get('recommended_certifications', []))}")
                    
                    tab_m1, tab_m2, tab_m3 = st.tabs(["📅 Days 1-30", "📅 Days 31-60", "📅 Days 61-90"])
                    with tab_m1:
                        for steps in roadmap_data.get("plan_30_days", []): st.markdown(f"- {steps}")
                    with tab_m2:
                        for steps in roadmap_data.get("plan_60_days", []): st.markdown(f"- {steps}")
                    with tab_m3:
                        for steps in roadmap_data.get("plan_90_days", []): st.markdown(f"- {steps}")
                        
            elif trigger_rewrite:
                with st.spinner("Refactoring project bullet structures..."):
                    rewrite_data = rewrite_resume(rag_context_resume)
                    st.session_state["active_resume_rewrite"] = rewrite_data
                    
                    st.markdown("### ✍️ Professional Experience Structural Adjustments")
                    st.markdown(f"**Optimized Stated Summary:**\n_{rewrite_data.get('optimized_summary')}_")
                    
                    with st.expander("📝 View Optimized Stated Projects & Achievements Bullet Adjustments"):
                        for bp in rewrite_data.get("rewritten_projects", []): st.markdown(f"* {bp}")
                    st.caption(f"**Target System Keywords To Inject:** {', '.join(rewrite_data.get('suggested_ats_keywords', []))}")
                    
            elif trigger_cover:
                with st.spinner("Drafting professional persuasive business text letter..."):
                    cover_letter_prose = generate_cover_letter(rag_context_resume, jd_text)
                    st.markdown("### 📝 Tailored Professional Business Letter")
                    st.text_area("Prose Copy Container Box", value=cover_letter_prose, height=350)
                    
            # --- ReportLab Export Actions Group ---
            if "active_report" in st.session_state:
                st.write("---")
                pdf_filename = f"Audit_Assessment_{resume_file.name}.pdf"
                pdf_filepath = f"outputs/{pdf_filename}"
                if st.button("Compile Downloadable PDF Compliance Verification Report", key="dl_report_btn"):
                    export_pdf_report(pdf_filename, st.session_state["active_report"], pdf_filepath)
                    with open(pdf_filepath, "rb") as f_stream:
                        st.download_button("📥 Save Assessment Report PDF", f_stream, file_name=pdf_filename, mime="application/pdf")

            if "active_resume_rewrite" in st.session_state:
                st.write("---")
                resume_filename = f"Optimized_Resume_{resume_file.name}"
                resume_filepath = f"outputs/{resume_filename}"
                if st.button("Compile & Export PDF Document of Rewritten Resume", key="dl_resume_btn"):
                    export_rewritten_resume_pdf(resume_filename, st.session_state["active_resume_rewrite"], resume_filepath)
                    with open(resume_filepath, "rb") as f_resume_stream:
                        st.download_button("📥 Download Rewritten Resume PDF", f_resume_stream, file_name=resume_filename, mime="application/pdf")
        else:
            st.info("Awaiting file drops. Upload matching PDF profiles or paste description elements inside the layout panel to unlock calculations.")

# ==========================================
# 📜 WORKSPACE SUITE 2: INSTITUTIONAL ANALYTICS LOGS
# ==========================================
elif navigation_tab == "Institutional Analytics Logs":
    st.subheader("📜 System Historic Compliance Audits Database Records")
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT NAME, ATS_SCORE, MATCH_PERCENTAGE, ANALYSIS_DATE FROM CANDIDATE_ANALYSIS ORDER BY ID DESC;")
        log_rows = cursor.fetchall()
        
    if log_rows:
        df_logs = pd.DataFrame(log_rows, columns=["Candidate Staged File Name", "ATS Diagnostic Score", "Domain Skill Match Weight %", "Analysis Generation Timestamp"])
        col_m1, col_m2 = st.columns(2)
        with col_m1: st.metric("Total Corporate Profile Appraisals Executed", len(df_logs))
        with col_m2: st.metric("Mean System Selection Matching Metric Score", f"{round(df_logs['ATS Diagnostic Score'].mean(), 1)} / 100")
        st.write("---")
        st.dataframe(df_logs, use_container_width=True)
    else:
        st.info("Tracking database contains zero processed candidate logs at this operational checkpoint.")