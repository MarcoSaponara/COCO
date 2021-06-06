#!/bin/bash
root=$(pwd)
source "${root}/venv/bin/activate"
(echo "import sys" ; echo "print(sys.prefix)") | python
cd ./ctrl
if test "$#" -eq 5; then
    python generation.py --model_dir seqlen256_36layers_v0.ckpt --temperature $1 --topk $2 --print_once --generate_num $3 --n_sentences $4 --prompt_list $5
fi
if test "$#" -eq 6; then
    python generation.py --model_dir seqlen256_36layers_v0.ckpt --temperature $1 --topk $2 --print_once --generate_num $3 --n_sentences $4 --prompt_list $5 --output_file $6
fi