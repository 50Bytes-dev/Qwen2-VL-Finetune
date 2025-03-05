#!/bin/bash

MODEL_NAME="Qwen/Qwen2-VL-7B-Instruct"
# MODEL_NAME="Qwen/Qwen2-VL-2B-Instruct"

export PYTHONPATH=src:$PYTHONPATH

python src/merge_lora_weights.py \
    --model-path /root/Qwen2-VL-Finetune/output/qwen_2.5_lora \
    --model-base $MODEL_NAME  \
    --save-model-path /root/Qwen2-VL-Finetune/output/qwen_2.5_merge \
    --safe-serialization