#!/bin/bash

export PYTHONPATH=src:$PYTHONPATH

python src/awq_quantize.py \
    --model-path SoBytes/Sadovod-VL-7B \
    --quant-path /root/Qwen2-VL-Finetune/output/qwen_2.5_awq \
    --token your_token_[optional]