
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
