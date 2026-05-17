# Gemini Vision Assistant

Gemini Vision Assistant is a lightweight multimodal AI system built using Google Gemini.

It enables:
- image understanding
- question answering on images
- structured multimodal reasoning
- CLI and API-based usage

---

# Features

- Image understanding using Gemini
- Question answering on visual inputs
- Lightweight multimodal processing
- CLI interface for quick testing
- FastAPI support for integration
- Evaluation framework for validation
- Optimization framework for improvement

---

# Why This Repository

Modern AI systems are evolving from:

```text
text-only generation
```

to:

```text
multimodal understanding (text + images)
```

This repository demonstrates how to build:
- practical multimodal AI systems
- production-style workflows
- Google-aligned AI applications

without relying on heavy frameworks.

---

# Architecture Overview

```text
Image + Question
        ↓
Vision Processor
        ↓
Gemini Vision Model
        ↓
Response Generation
        ↓
API / CLI Output
```

---

# Setup

Clone repository:

```bash
git clone <repo_url>
cd gemini-vision-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```text
GEMINI_API_KEY=your_key
MODEL_NAME=gemini-1.5-flash
```

---

# CLI Usage

```bash
python -m app.cli --image data/sample.jpg --question "What is in the image?"
```

---

# API Usage

Start server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Example Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{"image_path":"data/sample.jpg","question":"What is happening in the image?"}'
```

---

# Evaluation

Run evaluation:

```bash
python -m evaluation.evaluator
```

Run optimizer:

```bash
python -m evaluation.optimizer
```

---

# Evaluation Scope

The system evaluates:
- correctness of image understanding
- presence of expected concepts
- basic reasoning quality

---

# Google Ecosystem Alignment

This repository is built using Google Gemini and aligns with modern Google AI workflows.

It demonstrates:
- multimodal reasoning
- image understanding
- structured prompt engineering
- lightweight AI system design

Inspired by:
- Google Gemini Cookbook
- Google AI Studio
- modern Google GenAI patterns

---

# Use Cases

- visual assistants
- image-based Q&A systems
- multimodal AI experimentation
- Google Gemini exploration
- AI prototype development

---

# Limitations

- basic evaluation approach
- no OCR support
- no document ingestion
- no UI
- single-image processing only

---

# Future Improvements

- document understanding (PDF + OCR)
- multimodal RAG systems
- streaming responses
- UI interface
- multi-turn interactions
- semantic evaluation

---

# Design Philosophy

This repository is intentionally designed as:

```text
Small but powerful multimodal AI system
```

focusing on:
- clarity
- modularity
- real-world capability
- Google-aligned experimentation

---

Built using Google Gemini for modern multimodal AI systems.
