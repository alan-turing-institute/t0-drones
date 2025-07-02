import os
import tiktoken

# Choose the correct encoding for the model
encoding = tiktoken.encoding_for_model("gpt-4")

tot = 0

for file in os.listdir("data"):
    if file.endswith(".txt"):
        with open(os.path.join("data", file), "r", encoding="utf-8") as f:
            content = f.read()
            tokens = encoding.encode(content)
            tot += len(tokens)
print(f"Total tokens in all text files: {tot}")
