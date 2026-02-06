import math
import torch
import json
from transformers import GPT2LMHeadModel, AutoTokenizer
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling
from preprocess import hf_datasets
import os

os.makedirs("Epstein-LLM", exist_ok=True)

tokenized_data = hf_datasets(
    "sleeping-ai/Epstein-Emails",
    "sleeping-ai/enron-emails",
    eval_size=0.2
)

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=192,
    per_device_eval_batch_size=192,
    eval_strategy="epoch",
    save_strategy="epoch",
    warmup_steps=500,
    weight_decay=0.01,
    load_best_model_at_end=True,
    logging_dir="./logs",
    logging_steps=50,
    bf16=True,
    report_to="none",
    remove_unused_columns=False,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data["train"],
    eval_dataset=tokenized_data["test"],
    data_collator=data_collator,
)

trainer.train()

results = trainer.evaluate()
perplexity = math.exp(results["eval_loss"])
print("Perplexity:", perplexity)

results_to_save = {
    "eval_loss": results["eval_loss"],
    "perplexity": perplexity
}
with open("./Epstein-LLM/eval_results.json", "w") as f:
    json.dump(results_to_save, f, indent=4)

model.save_pretrained("./Epstein-LLM")
tokenizer.save_pretrained("./Epstein-LLM")


