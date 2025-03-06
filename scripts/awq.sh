#!/bin/bash

export PYTHONPATH=src:$PYTHONPATH

python src/merge_lora_weights.py \
    --model-path /root/Qwen2-VL-Finetune/output/qwen_2.5_merge \
    --quant-path /root/Qwen2-VL-Finetune/output/qwen_2.5_awq \
    --token my_hf_token