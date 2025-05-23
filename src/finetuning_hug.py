import pandas as pd
from sklearn.preprocessing import LabelEncoder
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import numpy as np
import torch
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Charge dataset
def load_data(): 
    df = pd.read_csv("lyrics.csv")
    return df

df = load_data()

return df

df = load_data()

# Encode labels
label_encoder = LabelEncoder()
df["Titre + artist"] = label_encoder.fit_transform(df["Genre"])
label_list = label_encoder.classes_.tolist()

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(df[["Parole", "Titre + artist"]])

# Tokenization
model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def tokenize_function(example):
    return tokenizer(example["Parole"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.2)
tokenized_dataset.set_format("torch")

# Load model
model = AutoModelForSequenceClassification.from_pretrained(
    model_checkpoint,
    num_labels=len(label_list),
    id2label={i: l for i, l in enumerate(label_list)},
    label2id={l: i for i, l in enumerate(label_list)}
)

# Training arguments
training_args = TrainingArguments(
    output_dir="results_hugface",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy"
)

# Metrics
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average="weighted"),
        "precision": precision_score(labels, preds, average="weighted"),
        "recall": recall_score(labels, preds, average="weighted"),
    }

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

# Train
trainer.train()

# Evaluate
metrics = trainer.evaluate()
print("Évaluation du modèle :", metrics)

# Save final model
trainer.save_model("lyrics_classifier_model")
tokenizer.save_pretrained("lyrics_classifier_model")
