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

## Installation

To set up the project locally:

```bash
git clone https://github.com/yourusername/customer-service-evaluator.git
cd customer-service-evaluator
pip install -r requirements.txt
```

## Usage

1. **Start the app**:

   ```bash
   python app.py
   ```
2. **Upload your CSV** file with columns: `chat_log`, `coherence`, `relevance`, `politeness`, `resolution`.
3. **Visit** `http://localhost:7860` in your browser.
4. **Explore** the dashboard to view metrics, summaries, and reports.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Developed by Hussien et al., Nile University (2025)*
