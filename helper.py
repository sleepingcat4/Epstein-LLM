def count_tokens(batch):
    return {"token_count": [sum(mask) for mask in batch["attention_mask"]]}