import json
import pandas as pd
import re
from tqdm import tqdm

class EpsteinFiles:
    @staticmethod
    def clean_data(input_path, output_path="epstein_train.txt", min_len=200):
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        output = open(output_path, "w", encoding="utf-8")
        header_pattern = re.compile(r"^(From|To|Sent|Subject|Attachments):.*$", re.MULTILINE)
        signature_pattern = re.compile(r"(Regards,.*|Best,.*|Sincerely,.*|--.*|This message,.*|Phone:.*)", re.IGNORECASE)

        for item in tqdm(data, desc="cleaning epstein emails"):
            text = item.get("email_text", "")
            if not text:
                continue

            text = re.sub(header_pattern, "", text)
            text = re.sub(signature_pattern, "", text)
            text = re.sub(r"HOUSE OVERSIGHT \d+", "", text)
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"[^a-zA-Z0-9\s.,!?;:'\"()-]", " ", text)
            text = text.strip()

            if len(text.split()) < min_len:
                continue

            output.write(text + "\n")

        output.close()


class EnronEmail:
    @staticmethod
    def clean_data(input_path, output_path="enron_emails.txt", text_column="message", min_len=200):
        df = pd.read_csv(input_path)
        output = open(output_path, "w", encoding="utf-8")
        header_pattern = re.compile(r"(?i)^(Message-ID|Date|From|To|Cc|Bcc|Subject):.*$", re.MULTILINE)
        signature_pattern = re.compile(r"(Regards,.*|Best,.*|Sincerely,.*|--.*|This message,.*|Confidential.*)", re.IGNORECASE)

        for text in tqdm(df[text_column].fillna(""), desc="cleaning enron emails"):
            if not text:
                continue

            text = re.sub(header_pattern, "", text)
            text = re.sub(signature_pattern, "", text)
            text = re.sub(r"<.*?>", " ", text)
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"[^\w\s.,!?;:'\"()-]", " ", text)
            text = text.strip()

            if len(text.split()) < min_len:
                continue

            output.write(text + "\n")

        output.close()

EpsteinFiles.clean_data("E:\Paper\Epstein\emails_dataset.json")