from huggingface_hub import snapshot_download
from mlx_lm import load, generate

REPO = "mlx-community/Llama-3.2-3B-Instruct-4bit"
try:
    path = snapshot_download(REPO, local_files_only=True)
    print("Model already downloaded.")
except Exception:
    print("Model not found locally. Downloading...")
    path = snapshot_download(REPO)
    print("Download complete.")

model, tokenizer = load(path)

while True:
    prompt = input("\nPrompt (or 'quit'): ").strip()
    if prompt.lower() in ("quit", "exit"):
        break
    if not prompt:
        continue
    messages = [{"role": "user", "content": prompt}]
    formatted = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    print(generate(model, tokenizer, prompt=formatted))