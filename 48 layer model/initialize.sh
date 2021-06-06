#!/bin/bash
root=$(pwd)
mkdir -p CTRL\ Project_48\ Layers
cd ./CTRL\ Project_48\ Layers
python -m venv venv
source "${root}/CTRL Project_48 Layers/venv/bin/activate"
${root}/CTRL\ Project_48\ Layers/venv/bin/python -m pip install --upgrade pip
(echo "import sys" ; echo "print(sys.prefix)") | python
pip install tensorflow-gpu==1.14
git clone https://github.com/salesforce/ctrl
pip show tensorflow_estimator
(echo "import os" ; echo "print(os.listdir('${root}/CTRL Project_48 Layers/venv/lib/python3.6/site-packages/tensorflow_estimator/python/estimator/'))") | python
cd ./ctrl
patch -b ${root}/CTRL\ Project_48\ Layers/venv/lib/python3.6/site-packages/tensorflow_estimator/python/estimator/keras.py estimator.patch
pip install fastBPE
pip install gsutil
gsutil -m cp -r gs://sf-ctrl/seqlen256_v1.ckpt/ .
