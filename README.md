
🔧 Tools Used
In this project, three tools are utilized for tasks:

pyLDAvis for topic modeling visualization.

SnowNLP for sentiment analysis and Chinese text processing.

MING for advanced medical NER using large pre-trained models.

## 🏃‍♂️ Quick Start

Here are the steps for setting up the environment and using the tools for NER tasks.

### Step 1: Install the Environment

Install the following dependencies:


```bash
python==3.9.16
pytorch==2.0.1+cu117
peft==0.9.0
```
### Step 2: Use the Tools for NER

####  **pyLDAvis** for Topic Modeling 

If you need to visualize the topics in the dataset, install **pyLDAvis**:

```bash
pip install pyldavis
```

Then use it to visualize topics after fitting a topic model.

####  **SnowNLP** for Sentiment Analysis

**SnowNLP** can be used for processing Chinese text and performing sentiment analysis.

Install SnowNLP:

```bash
pip install snownlp
```

Example code for sentiment analysis:

```python
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')
print(s.sentiments)  # Sentiment score: 0 (negative) to 1 (positive)
```
#### **MING** for Medical NER

To run **MING** for NER tasks, use the following commands:

1. Install and load the model:

```bash
CUDA_VISIBLE_DEVICES=0 python -m ming.serve.cli \
    --model_path {path_to_checkpoint} \
    --model_base {path_to_base_model} \
    --max_new_token 3072
```

2. Run the model for NER:

```python
input_text = "患者主诉头痛三天，服用布洛芬后缓解不明显。"
ner_output = model.predict(input_text)  # Sample code to predict NER output
print(ner_output)
```

---

Contributions and improvements are welcome!
