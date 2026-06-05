# 💼 Enterprise AI Resume ATS Analyzer & Placement Hub

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.45.1-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Vector Engine](https://img.shields.io/badge/FAISS-CPU%201.11.0-004A7F?style=for-the-badge&logo=databricks&logoColor=white)](https://github.com/facebookresearch/faiss)
[![Primary LLM](https://img.shields.io/badge/Gemini%202.5-Flash-0066FF?style=for-the-badge&logo=google-gemini&logoColor=white)](https://ai.google.dev/)
[![Failover Core](https://img.shields.io/badge/Groq-Llama%203.3-F55036?style=for-the-badge&logo=meta&logoColor=white)](https://groq.com/)

An enterprise-grade, asymmetric Retrieval-Augmented Generation (RAG) agentic pipeline engineered to reverse-engineer Application Tracking System (ATS) matching patterns. By coupling **Gemini 2.5 Flash** structured json-schema emission with a local dense vector proximity space managed by **FAISS**, this hub transforms unstructured resume data into actionable career metrics, custom interview simulations, and pristine application components.

---

## 📺 Live Video Demonstration & Interface Walkthrough

> 💡 **Engineering Reviewers & Recruiters:** Watch the core architectural execution sequence, real-time context fetching loops, and downstream compilation actions in real time:

```mermaid
%% System Walkthrough Timeline
graph LR
    A[1. Multi-Input Ingestion] --> B[2. Dense Vector Extraction] --> C[3. Resilient Failover Generation] --> D[4. ReportLab PDF Export]

🎬 System Walkthrough Video
https://github.com/UpayanChatterjee/AI-Resume-ATS-Analyzer-Assistance/assets/demo-video.mp4

📂 To preview your live workspace video stream, record a short clip of your application in action, drag-and-drop the .mp4 into your GitHub repository root, and match its path reference to the link above.

📸 Production-Ready Core Operational Showcases
<img width="1917" height="876" alt="image" src="https://github.com/user-attachments/assets/da523293-684f-48a2-a0c2-5d1fbba0fc06" />

<img width="1917" height="877" alt="image" src="https://github.com/user-attachments/assets/da864fa0-7283-44ec-b178-c383880b2997" />

<img width="1912" height="870" alt="image" src="https://github.com/user-attachments/assets/6cc8666a-bdda-443b-bbd3-65be13d9d9fd" />



1. Unified Diagnostic Assessment Suite Workspace
Dual-mode operational panel allowing seamless file drops or copy-paste text ingestion processing alongside real-time interactive Plotly matching gauges.

2. Contextual Interview Preparation & Microservice Triggers
Schema-enforced interview simulation engines mapping custom technical drills, behavioral criteria, and project architectural reviews.

3. Institutional Placement Analytics Log
Permanent relational state retention engine logging analysis timestamps, transaction metrics, and score distributions via an isolated SQLite database layer.



🗺️ System Architecture & Data Flow
The platform separates data extraction, semantic search vector storage, and state preservation to optimize request-response latencies and secure strict data alignment boundaries:


[ Raw Candidate Profile PDF ]      [ Corporate Job Specification (PDF/Text) ]
                   │                                        │
                   ▼                                        ▼
       ┌──────────────────────┐                  ┌──────────────────────┐
       │   pypdf Extraction   │                  │  Ingestion Filter    │
       └──────────┬───────────┘                  └──────────┬───────────┘
                  │                                         │
                  ▼ (Raw Text Payload Segment)              │
       ┌──────────────────────┐                             │
       │ sentence-transformers│                             │
       └──────────┬───────────┘                             │
                  │                                         │
                  ▼ (768-Dim Spatial Embeddings)            │
       ┌──────────────────────┐                             │
       │   FAISS Vector DB    │                             │
       └──────────┬───────────┘                             │
                  │                                         │
                  ▼ (Local Semantic Context Neighborhood)   │
       ┌────────────────────────────────────────────────────┴───────────┐
       │ Orchestration Layer, Multi-Agent Prompts & State Evaluators     │
       └────────────────────────────┬───────────────────────────────────┘
                                    │
               ┌────────────────────┴────────────────────┐
               ▼ (Primary Engine Attempt)                ▼ (On HTTP 503 Traffic Overload)
    ┌───────────────────────────────┐        ┌───────────────────────────────┐
    │       Gemini 2.5 Flash        │───────>│       Groq Llama 3.3          │
    │  (Structured JSON Compliance) │        │   (High-Throughput Failover)  │
    └──────────────┬────────────────┘        └──────────────┬────────────────┘
                   │                                        │
                   └───────────────────┬────────────────────┘
                                       │
                                       ▼ (Validated Structured Schema Payload)
                   ┌───────────────────┴───────────────────┐
                   │               App Layer               │
                   └─┬───────────────────────────────────┬─┘
                     │                                   │
                     ▼ (Transactional Cache)             ▼ (Binary Stream Render)
       ┌───────────────────────────┐       ┌───────────────────────────┐
       │     SQLite3 Database      │       │  ReportLab PDF Compilers  │
       │  [ CANDIDATE_ANALYSIS ]   │       │ [ Traditional Resumes ]   │
       └───────────────────────────┘       └───────────────────────────┘




📂 Codebase Modular Layout
{i will provide ss or line diagram}




💾 Institutional Relational Data Schema
Candidate evaluation scores, match criteria, and audit histories are persistently stored inside a lightweight relational database schema managed locally:

Table Specification: CANDIDATE_ANALYSIS

https://docs.google.com/spreadsheets/d/1jT5eEfcrD5Lw29XSrxSca5Jl8gr9q9b0Y3UF8cdVMpE/edit?usp=sharing





🚀 Rapid Local Deployment Guide
1. Clone Repository & Target Workspace
Open your system terminal, navigate to your development directory, and clone the assets:

Bash
git clone [https://github.com/UpayanChatterjee/AI-Resume-ATS-Analyzer-Assistance.git](https://github.com/UpayanChatterjee/AI-Resume-ATS-Analyzer-Assistance.git)
cd AI-Resume-ATS-Analyzer-Assistance
2. Isolate and Spin Up Your Virtual Environment
To prevent package version collision, construct a isolated sandbox environment using Python 3.10 or 3.11:

Bash
# Initialize Environment
python -m venv venv

# Activate Environment (Windows Command Prompt Architecture)
venv\Scripts\activate

# Activate Environment (macOS / Linux Shell Architecture)
source venv/bin/activate
3. Clean Batch Installation of Stack Requirements
Run the mass dependency ingestion sequence directly from the production matrix mapping:

Bash
pip install -r requirements.txt
4. Inject Environmental Variables
Create an file named exactly .env in the root directory workspace and drop your authorization keys inside:

Code snippet
GEMINI_API_KEY=AIzaSyYourSecretKeyStringHere
GROQ_API_KEY=gsk_YourSecretGroqKeyStringHere
5. Boot Up the Dashboard Web Portal
Kickstart the local server container framework to spin up the interface:

Bash
streamlit run app.py
🛡️ License Architecture
Distributed under the MIT License. Check out the repository root documentation to read explicit liability exclusions and open engineering utilization clearances.


