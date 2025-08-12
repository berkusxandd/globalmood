import os
from huggingface_hub import InferenceClient

MAX_LENGTH = 514

def truncate_text(text, max_len=MAX_LENGTH):
    return text[:max_len]

client = InferenceClient(
        provider="hf-inference",
        api_key=os.environ["HF_TOKEN"],
    )


def analyze_sentiment(sentence):
    sentence = truncate_text(sentence)
    result = client.text_classification(
        sentence,
        model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    )
    return result



