# AI-Powered Customer Service Evaluator

**Graduate Project | AI & NLP**

---

## Overview

This web application evaluates **customer service chat logs** between agents and customers, quantifying agent performance across four key metrics:

* **Coherence** (1–5)
* **Relevance** (1–5)
* **Politeness** (1–5)
* **Resolution** (0 or 1)

By automating these evaluations, the system delivers objective insights into agent performance and highlights areas for improvement.

## Dataset

We introduce a novel dataset of **2,500** annotated examples:

* **2,000** chat logs for fine-tuning
* **500** chat logs for evaluation

Each entry contains:

1. Full chat transcript (agent and customer)
2. Numerical scores for coherence, relevance, politeness, and resolution

All data is anonymized and compliant with privacy regulations.

## Architecture & Multi-Agent Pipeline

The system uses a **multi-agent** architecture with three specialized components:

### 1. Metric Evaluator Agent

Computes all four performance metrics for each chat log.

### 2. Insight Generator Agent

Summarizes evaluation results, identifies trends, and generates personalized recommendations for agents.

### 3. Reporting Agent

Aggregates metrics into dashboards and reports, enabling managers to monitor team performance.

```text
[ Chat Log Input ]
         │
         ▼
┌────────────────────────────┐
│ Metric Evaluator Agent     │
└────────────────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Insight Generator Agent    │
└────────────────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Reporting Agent            │
└────────────────────────────┘
         │
         ▼
[ Performance Dashboard ]
```

