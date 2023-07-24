# from transformers import pipeline
#
# generator=pipeline('text-generation', model='gpt2')
# result = generator("how are you", max_length=30, num_return_sequences=5)
# # to pretty show the json result
# import json
# print(json.dumps(result, indent=4))
# # print(result)


# from transformers import GPTNeoXForCausalLM, AutoTokenizer
#
# tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
# model = GPTNeoXForCausalLM.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
#
# message = "<|prompter|>Hello

# Use a pipeline as a high-level helper
from transformers import pipeline
import xformers


# Setting `pad_token_id` to `eos_token_id`:0 for open-end generation.


# pipe = pipeline("text-generation", model="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
# result = pipe("Hello, I'm a language model,", max_length=50, num_return_sequences=1, pad_token_id=0)
# print(result)

# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="bigscience/bloom")
result = pipe("Hello, I'm a language model,")
print(result)