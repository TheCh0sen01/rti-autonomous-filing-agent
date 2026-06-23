# RTI Autonomous Filing Agent

An AI-powered autonomous system designed to simplify and automate the **Right to Information (RTI)** filing process in India.

This project was built with the idea that filing RTIs should not require users to understand complex government workflows, department hierarchies, or legal drafting formats. The system bridges that gap by combining **LLMs, Retrieval-Augmented Generation (RAG), workflow orchestration, and automation pipelines** to transform raw complaints into legally structured RTI applications.

---

## Problem Statement

Many citizens face challenges when filing RTIs:

* Lack of awareness about the correct department
* Difficulty identifying the Public Information Officer (PIO)
* Poorly drafted applications leading to rejection
* Missed appeal deadlines
* Complex portal workflows

This system automates that entire lifecycle.

---

# System Architecture

User Input (Text / Voice / Regional Language)
↓
Intent Extraction
↓
Issue Classification
↓
Department Mapping
↓
RTI Draft Generation
↓
Risk Analysis
↓
Multi-Channel Filing
↓
Deadline Tracking
↓
Appeal Automation

---

# Core Features

## 1. Multi-Modal Complaint Intake

Supports:

* Text input
* Voice input
* Multiple Indian languages

Pipeline:

* Whisper for speech-to-text
* Language detection
* Intent classification
* Structured issue extraction

Extracted fields:

* Issue type
* Location
* Severity
* Department hint
* Language

Example:

```json
{
  "issue_type": "ration card delay",
  "location": "Chennai",
  "severity": "medium",
  "language": "English"
}
```

---

## 2. Department Intelligence Engine

Maps complaints to:

* Ministry
* Department
* PIO
* Office Address
* Contact Email

Uses:

* ChromaDB vector search
* Sentence-transformer embeddings
* Department knowledge base

Capabilities:

* Semantic similarity search
* Department resolution
* Contact discovery

Coverage:

* 50+ mapped departments

---

## 3. RTI Draft Generator

Automatically generates:

* Legally compliant RTI applications
* Department-specific templates
* Proper question framing

Knowledge Sources:

* RTI Act 2005
* CIC guidelines
* Appeal templates
* Court references

Powered by:

* Ollama (Qwen 3 / Llama 3.1)
* LangChain
* Few-shot prompting

---

## 4. Risk & Compliance Review

Pre-submission validation for:

* Privacy violations
* Section 8 exemptions
* Personal data requests
* Ambiguous wording

Output:

```json
{
  "risk_score": 0.08,
  "status": "Safe"
}
```

---

## 5. Multi-Channel Filing System

### Email Filing

Primary channel using Gmail API.

Flow:

Draft → PDF → Email → PIO

---

### Portal Filing (Experimental)

Automated filing via Playwright.

Features:

* Form autofill
* CAPTCHA detection
* Human fallback

---

### Manual Filing

Professional PDF generation for offline submission.

Libraries:

* ReportLab
* python-docx

---

## 6. Deadline Tracker

Tracks:

* RTI filing date
* 30-day deadline
* Reminder notifications
* Response status

Storage:

* SQLite

Scheduling:

* APScheduler

---

## 7. Escalation Engine

Automates:

* First Appeal
* Second Appeal

If deadlines are missed.

Uses:

* LangGraph
* ChromaDB
* Appeal templates

Generates:

* Appeal drafts
* Evidence package
* Timeline summary

---

## 8. Analytics Dashboard

Tracks:

* Total RTIs filed
* Department response rates
* Appeal rates
* Pending requests
* Monthly filing history

Built with:

* Streamlit
* Pandas
* Matplotlib

---

# Tech Stack

## AI / LLM

* Ollama
* LangChain
* LangGraph
* Whisper
* Sentence Transformers

## Storage

* ChromaDB
* SQLite
* Supabase

## Automation

* Playwright
* Gmail API

## Backend

* Python
* FastAPI

## Dashboard

* Streamlit

## Document Generation

* ReportLab
* python-docx

---

# Why This Project Matters

This is more than an AI project.

It is a civic-tech infrastructure system designed to improve transparency, accessibility, and accountability.

It reduces:

* procedural complexity
* filing friction
* legal drafting errors

while improving:

* citizen access
* filing quality
* escalation efficiency

---

# Future Improvements

* OCR support for government notices
* WhatsApp integration
* Auto-reply classification
* State-specific RTI workflows
* RTI success prediction model
* Public transparency heatmaps

---

