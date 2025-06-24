
# pyLDAvis


**pyLDAvis** is a Python library for interactive visualization of topic models, especially those built using **Latent Dirichlet Allocation (LDA)**. This project is a Python port of the excellent R package by Carson Sievert and Kenny Shirley.

## 🔍 Overview

Topic modeling is a powerful tool for uncovering hidden thematic structures in large collections of documents. However, interpreting the results of models like LDA can be challenging. **pyLDAvis** makes topic model outputs accessible and interpretable through interactive visualizations.

The visualization helps users explore:

- The relationship between topics
- The most relevant terms for each topic
- The distribution of terms across topics
- Topic saliency and distinctiveness

## 📘 Highlights

- Built for intuitive, web-based interpretation of topic models
- Automatically extracts and structures LDA model results
- Visualizes topic distances and term relevance using bar charts and inter-topic distances
- Compatible with Jupyter notebooks and exportable as standalone HTML

> Note: LDA stands for *Latent Dirichlet Allocation*, a common algorithm used for unsupervised topic modeling.

## 📦 Installation

Install the latest stable release using pip:

```bash
pip install pyldavis
```

## 📁 Output Example

The image above shows an example output of pyLDAvis, where:
- Circles represent topics
- The size of each circle indicates topic prevalence
- Bars indicate term relevance within a selected topic

---

Enjoy visualizing your topic models with **pyLDAvis**!

---

# SnowNLP: Sentiment Analysis for Simplified Chinese


**SnowNLP** is a Python library designed specifically for **processing and analyzing Simplified Chinese text**, inspired by the TextBlob library. Unlike TextBlob or NLTK-based tools, SnowNLP is fully self-contained and does not rely on external NLP libraries. It includes its own models and algorithms.

## 🔍 Sentiment Analysis

One of the core features of SnowNLP is **sentiment analysis**. This module can estimate how positive or negative a given sentence is, based on a built-in dataset. It is particularly effective for product reviews or similar domains.

### Example Usage

```python
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')
print(s.sentiments)  # e.g., 0.97 → very positive
```

The `sentiments` score ranges from **0 (very negative)** to **1 (very positive)**.

## ✨ Additional Features

While this README focuses on sentiment analysis, SnowNLP also supports:

- Chinese word segmentation
- Part-of-speech tagging
- Text summarization and keyword extraction
- Traditional to simplified conversion
- Text classification
- Text similarity scoring (BM25)

## 📦 Installation

Install SnowNLP via pip:

```bash
pip install snownlp
```

Enjoy analyzing Chinese text with **SnowNLP**!


# MING for Medical Named Entity Recognition (NER)

**MING** is an open-source Chinese medical large language model (LLM) fine-tuned with domain-specific medical instructions. While originally designed for multi-turn diagnosis and medical Q&A tasks, this project focuses on applying **MING to Chinese medical Named Entity Recognition (NER)**.

## 🧠 Project Overview

MING can identify critical medical entities from Chinese clinical texts, such as diseases, symptoms, drugs, and examinations. It is highly effective in tasks like medical knowledge graph construction, case structuring, and clinical decision support.

Example:

```text
Input Text: 患者主诉头痛三天，服用布洛芬后缓解不明显。
NER Output: 头痛 (Symptom), 布洛芬 (Drug)
```

## 🔍 Model Versions

| Model Name       | Base Model        | HuggingFace Link |
|------------------|-------------------|------------------|
| MING-7B          | bloomz-7b1-mt     | 🤗 MING-7B        |
| MING-1.8B        | Qwen1.5-1.8B      | 🤗 MING-1.8B      |
| MING-MOE-1.8B    | Qwen1.5-1.8B      | 🤗 MING-MOE-1.8B  |
| MING-MOE-4B      | Qwen1.5-4B        | 🤗 MING-MOE-4B    |
| MING-MOE-7B      | Qwen1.5-7B        | 🤗 MING-MOE-7B    |
| MING-MOE-14B     | Qwen1.5-14B       | 🤗 MING-MOE-14B   |

## 🚀 Quick Start

Environment requirements (adjust as needed):

```bash
python==3.9.16
pytorch==2.0.1+cu117
peft==0.9.0
```

---

Contributions and improvements are welcome!

