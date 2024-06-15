import datasets 
datasets.logging.set_verbosity_error()

from datasets import load_dataset

dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Amazon_Fashion", trust_remote_code=True)

print(dataset["full"][0])
