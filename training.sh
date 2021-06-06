#!/bin/bash
root=$(pwd)
source "${root}/venv/bin/activate"
(echo "import sys" ; echo "print(sys.prefix)") | python
cd ./ctrl/training_utils
yes | pip uninstall gast
pip install gast==0.2.2
pip install tqdm
python make_tf_records.py --text_file $1 --control_code $2 --sequence_len 256
if test "$#" -eq 3; then
    python training.py --model_dir ../seqlen256_v1.ckpt/ --iterations $3 --learning_rate 1e-2
fi
if test "$#" -eq 4; then
    python training.py --model_dir ../seqlen256_v1.ckpt/ --iterations $3 --learning_rate $4
fi
