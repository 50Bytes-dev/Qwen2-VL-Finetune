import argparse
import huggingface_hub
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer


def awq(args):
    if args.token:
        huggingface_hub.login(token=args.token)

    model_path = args.model_path
    quant_path = args.quant_path
    quant_config = {
        "zero_point": True,
        "q_group_size": 128,
        "w_bit": 4,
        "version": "GEMM",
    }

    # Load model
    model = AutoAWQForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

    # Quantize
    model.quantize(tokenizer, quant_config=quant_config)

    # Save quantized model
    model.save_quantized(quant_path)
    tokenizer.save_pretrained(quant_path)

    print(f'Model is quantized and saved at "{quant_path}"')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, required=True)
    parser.add_argument("--quant-path", type=str, required=True)
    parser.add_argument("--token", type=str, required=False)

    args = parser.parse_args()

    awq(args)
