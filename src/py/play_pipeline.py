from transformers import pipeline
import torch
classifier = pipeline('sentiment-analysis')
# classifier('We are very happy to show you the 🤗 Transformers library.')
# results = classifier(["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."])
results = classifier(["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it.", "I want to kill the bloody dog"])
print(results)