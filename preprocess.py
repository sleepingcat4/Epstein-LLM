from datasets import load_dataset, concatenate_datasets
from transformers import AutoTokenizer

def hf_datasets(*ds_names, eval_size=None, model_name="gpt2"):
    if isinstance(ds_names, str):
        ds_names = [ds_names]
        
    datasets = [load_dataset(name, split="train") for name in ds_names]
    dataset = concatenate_datasets(datasets).shuffle(seed=42)
    if eval_size and 0 < eval_size < 1:
        dataset = dataset.train_test_split(test_size=eval_size)
        
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    def tokenize_fn(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=512)
    cols_to_remove = dataset.column_names if not eval_size else dataset["train"].column_names
    
    tokenized = dataset.map(
        tokenize_fn, 
        batched=True,
        remove_columns=cols_to_remove,
        desc="Tokenizing dataset"
    )
    
    return tokenized