# 💼 Enterprise AI Resume ATS Analyzer & Placement Hub

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-CPU%201.11.0-004A7F?style=for-the-badge\&logo=databricks\&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%202.5%20Flash-0066FF?style=for-the-badge\&logo=google-gemini\&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3-F55036?style=for-the-badge\&logo=meta\&logoColor=white)

### AI-Powered ATS Analysis, Resume Optimization, Interview Preparation & Placement Assistance Platform

*Built using Retrieval-Augmented Generation (RAG), FAISS Semantic Search, Gemini 2.5 Flash, Groq Llama 3.3, Streamlit, SQLite, and ReportLab.*

</div>

---

# 📌 Overview

The **Enterprise AI Resume ATS Analyzer & Placement Hub** is an intelligent career-assistance platform designed to bridge the gap between job seekers and modern Applicant Tracking Systems (ATS).

Traditional ATS platforms evaluate resumes through keyword matching, skill relevance, project alignment, and contextual similarity with job descriptions. This system reverse-engineers that workflow using a Retrieval-Augmented Generation (RAG) architecture to provide actionable insights and improve application success rates.

The platform transforms unstructured resumes into structured career intelligence by:

* Analyzing ATS compatibility
* Identifying missing skills
* Generating improvement recommendations
* Producing interview preparation roadmaps
* Creating tailored interview questions
* Tracking candidate evaluations historically
* Generating downloadable reports

---

# 🎯 Key Features

### 📄 ATS Resume Analysis

* Resume parsing from PDF documents
* ATS compatibility scoring
* Job description matching
* Keyword coverage analysis
* Missing skill identification

### 🔍 Semantic Search with FAISS

* Dense vector embeddings
* Context-aware similarity retrieval
* Semantic resume-job matching
* Local vector database indexing

### 🤖 Multi-LLM Orchestration

* Primary Engine: Gemini 2.5 Flash
* Automatic Failover: Groq Llama 3.3
* Structured JSON output validation
* High availability response generation

### 🎤 AI Interview Preparation

* Technical interview questions
* Behavioral interview questions
* Project-specific interview drills
* Personalized preparation plans

### 📊 Candidate Analytics

* Historical ATS score tracking
* Resume analysis logs
* Performance trend monitoring
* Persistent storage using SQLite

### 📑 Report Generation

* ATS assessment reports
* Downloadable PDF resumes
* Career improvement summaries
* Recruiter-friendly outputs

---

# 🏗️ System Architecture

The platform follows a layered Retrieval-Augmented Generation (RAG) architecture that separates ingestion, retrieval, reasoning, and persistence components.

```text
[ Resume PDF ]                     [ Job Description ]
       │                                   │
       ▼                                   ▼

┌─────────────────┐          ┌─────────────────┐
│ PDF Extraction  │          │ Text Ingestion  │
└────────┬────────┘          └────────┬────────┘
         │                            │
         ▼                            ▼

     Raw Resume Text          Raw JD Content
                │
                ▼

┌──────────────────────────────┐
│ Sentence Transformer Model   │
└──────────────┬───────────────┘
               │
               ▼

      768-Dimensional Embeddings
               │
               ▼

┌──────────────────────────────┐
│      FAISS Vector Store      │
└──────────────┬───────────────┘
               │
               ▼

 Semantic Context Retrieval Layer
               │
               ▼

┌────────────────────────────────────────────┐
│ Multi-Agent Prompt Orchestration Engine    │
└─────────────────┬──────────────────────────┘
                  │
       ┌──────────┴──────────┐
       ▼                     ▼

┌─────────────────┐   ┌─────────────────┐
│ Gemini 2.5Flash │   │ Groq Llama 3.3  │
│ Primary Engine  │   │ Failover Engine │
└────────┬────────┘   └────────┬────────┘
         └──────────┬──────────┘
                    ▼

      Structured JSON Responses
                    │
                    ▼

┌───────────────────────────────────────────┐
│               Application Layer           │
└───────────────┬───────────────┬───────────┘
                │               │

                ▼               ▼

      SQLite Database      ReportLab PDF
      Historical Logs      Report Builder
```

---

# 📸 Application Showcase

## 1️⃣ Unified ATS Analysis Dashboard

Upload resumes and job descriptions through a streamlined interface to receive real-time ATS insights and compatibility metrics.

<img width="1917" height="876" alt="image" src="https://github.com/user-attachments/assets/da523293-684f-48a2-a0c2-5d1fbba0fc06" />

---

## 2️⃣ AI Interview Preparation Workspace

Generate technical, behavioral, and project-based interview questions tailored to the candidate profile.

<img width="1912" height="870" alt="image" src="https://github.com/user-attachments/assets/6cc8666a-bdda-443b-bbd3-65be13d9d9fd" />

---

## 3️⃣ Historical Analytics & Tracking

Monitor previous ATS evaluations and performance trends through a persistent database layer.

<img width="1917" height="877" alt="image" src="https://github.com/user-attachments/assets/da864fa0-7283-44ec-b178-c383880b2997" />

---

# 🎥 Video Demonstration

Watch the complete workflow including:

* Resume ingestion
* Semantic retrieval
* ATS scoring
* Interview generation
* PDF report creation
* Database logging

### Demo Video

```

```

---

# 🧠 Core Technologies

| Category               | Technology                 |
| ---------------------- | -------------------------- |
| Frontend               | Streamlit                  |
| Programming Language   | Python                     |
| Embedding Engine       | Sentence Transformers      |
| Vector Database        | FAISS                      |
| Primary LLM            | Gemini 2.5 Flash           |
| Failover LLM           | Groq Llama 3.3             |
| Database               | SQLite3                    |
| PDF Processing         | PyPDF                      |
| PDF Generation         | ReportLab                  |
| Visualization          | Plotly                     |
| Environment Management | Python Virtual Environment |

---

# 📊 Technical Concepts Demonstrated

This project showcases practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Dense Embeddings
* Prompt Engineering
* Multi-Agent Workflows
* Structured LLM Outputs
* AI Failover Systems
* Database Persistence
* Resume Parsing
* ATS Optimization
* Document Intelligence
* Information Retrieval
* Enterprise Application Design

---

# 📂 Project Structure

```text
AI-Resume-ATS-Analyzer-Assistance
│
├── app.py
├── requirements.txt
├── .env
│
├── database/
│   ├── candidate_analysis.db
│
├── modules/
│   ├── ats_analyzer.py
│   ├── interview_generator.py
│   ├── vector_store.py
│   ├── report_generator.py
│   ├── llm_orchestrator.py
│
├── assets/
│   ├── dashboard.png
│   ├── interview.png
│   ├── analytics.png
│
├── generated_reports/
│
└── README.md
```

---

# 💾 Database Schema

Candidate analyses are stored locally using SQLite for auditability and historical tracking.

### Table: `CANDIDATE_ANALYSIS`

| Field             | Type     |
| ----------------- | -------- |
| id                | INTEGER  |
| candidate_name    | TEXT     |
| ats_score         | REAL     |
| skill_match_score | REAL     |
| interview_score   | REAL     |
| missing_skills    | TEXT     |
| recommendations   | TEXT     |
| timestamp         | DATETIME |

### Dataset Reference

Google Sheet:

```text
https://docs.google.com/spreadsheets/d/1jT5eEfcrD5Lw29XSrxSca5Jl8gr9q9b0Y3UF8cdVMpE
```

---

# ⚡ Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/UpayanChatterjee/AI-Resume-ATS-Analyzer-Assistance.git

cd AI-Resume-ATS-Analyzer-Assistance
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file named:

```text
.env
```

Add:

```env
GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>

GROQ_API_KEY=<YOUR_GROQ_API_KEY>
```

---

## 5. Launch Application

```bash
streamlit run app.py
```

---

# 🚀 Future Enhancements

* Multi-resume batch analysis
* Recruiter dashboard
* PostgreSQL integration
* Cloud deployment support
* Resume ranking system
* LinkedIn profile analysis
* Fine-tuned ATS scoring model
* LangGraph-based agent orchestration
* Dockerized deployment
* Kubernetes scalability support

---

# 📈 Impact

This platform demonstrates how Retrieval-Augmented Generation can be leveraged to create intelligent career-assistance systems that go beyond keyword matching and provide meaningful, contextual guidance for candidates.

The architecture combines semantic retrieval, structured reasoning, persistent analytics, and automated interview preparation into a unified ecosystem capable of supporting modern placement and recruitment workflows.

---

# 👨‍💻 Author

### Upayan Chatterjee

Aspiring Software Engineer | AI Enthusiast | Full-Stack Developer

**Skills:**

* Java
* Spring Boot
* Python
* React
* SQL
* AI/ML
* RAG Systems
* Vector Databases
* System Design

GitHub:

```text
https://github.com/upayan0
```

---

# 📜 License

This project is distributed under the MIT License.

Feel free to use, modify, and distribute the software in accordance with the license terms.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star.

Building intelligent systems, one project at a time.

</div>
