#!/bin/bash
root=$(pwd)
source "${root}/venv/bin/activate"
(echo "import sys" ; echo "print(sys.prefix)") | python
cd ./ctrl
if test "$#" -eq 6; then
    python generation.py --model_dir seqlen256_36layers_v0.ckpt --temperature $1 --topk $2 --print_once --generate_num $3 --n_sentences $4 --nucleus $5 --prompt_list $6
fi
if test "$#" -eq 7; then
    python generation.py --model_dir seqlen256_36layers_v0.ckpt --temperature $1 --topk $2 --print_once --generate_num $3 --n_sentences $4 --nucleus $5 --prompt_list $6 --output_file $7
fi
