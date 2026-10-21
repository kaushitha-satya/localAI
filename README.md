# localAI - Local Llama 3.2 Chat with MLX

A minimal command-line interface for running Llama 3.2 3B Instruct locally on Apple Silicon using the [MLX](https://github.com/ml-explore/mlx) framework. The script downloads a 4-bit quantized model from the Hugging Face Hub on first run, caches it locally, and starts an interactive prompt loop.

## Features

- Runs entirely on-device with no external API calls after the initial download
- Automatically downloads the model on first run and reuses the local cache afterwards
- Uses the model's built-in chat template for correctly formatted prompts
- Lightweight 4-bit quantized model suitable for machines with limited memory
- Simple interactive loop with clean exit commands

## Requirements

- A Mac with Apple Silicon (M1 or later), as MLX is optimized for Apple's unified memory architecture
- macOS 13.5 or later
- Python 3.9 or later
- Approximately 2 GB of free disk space for the model weights
- An internet connection for the initial model download

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kaushitha-satya/localai.git
   cd <your-repository>
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install mlx-lm huggingface_hub
   ```

## Usage

Run the script:

```bash
python main.py
```

On the first run, the model is downloaded from the Hugging Face Hub:

```
Model not found locally. Downloading...
Download complete.
```

On subsequent runs, the cached copy is used:

```
Model already downloaded.
```

Once the model is loaded, enter a prompt at the interactive prompt:

```
Prompt (or 'quit'): Explain what a hash table is in two sentences.
```

To exit, type `quit` or `exit`. Empty input is ignored.

## How It Works

1. **Model resolution.** The script calls `snapshot_download` with `local_files_only=True` to check for a cached copy. If none is found, it downloads the model from the Hugging Face Hub.
2. **Model loading.** `mlx_lm.load` loads the weights and tokenizer into memory.
3. **Prompt formatting.** Each user input is wrapped in a chat message and formatted using the tokenizer's chat template, with the generation prompt appended.
4. **Generation.** `mlx_lm.generate` produces a response, which is printed to the terminal.

## Configuration

The model is set by the `REPO` constant at the top of the script:

```python
REPO = "mlx-community/Llama-3.2-3B-Instruct-4bit"
```

Any compatible MLX-format model on the Hugging Face Hub can be substituted by changing this value. Larger models require more memory.

Downloaded models are stored in the default Hugging Face cache directory, typically `~/.cache/huggingface/hub`.

## Limitations

- Each prompt is handled independently. The script does not retain conversation history between turns.
- Generation parameters such as maximum tokens and temperature use the library defaults and are not currently configurable from the command line.
- MLX targets Apple Silicon and is not intended for Intel-based Macs, Windows, or most Linux systems.

## Possible Improvements

- Maintain conversation history across turns
- Add command-line arguments for model selection, temperature, and maximum token count
- Stream tokens to the terminal as they are generated

## License and Model Terms

The license for this repository's code is specified in the `LICENSE` file. The Llama 3.2 model is distributed by Meta under the [Llama 3.2 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE). Review its terms before using the model in any application.

## Acknowledgments

- [MLX](https://github.com/ml-explore/mlx) and [mlx-lm](https://github.com/ml-explore/mlx-lm) by Apple
- [mlx-community](https://huggingface.co/mlx-community) for the quantized model conversion
- Meta for the Llama 3.2 model family
