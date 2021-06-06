#!/bin/bash
root=$(pwd)
mkdir -p CTRL\ Project_36\ Layers
cd ./CTRL\ Project_36\ Layers
python -m venv venv
source "${root}/CTRL Project_36 Layers/venv/bin/activate"
${root}/CTRL\ Project_36\ Layers/venv/bin/python -m pip install --upgrade pip
(echo "import sys" ; echo "print(sys.prefix)") | python
pip install tensorflow-gpu==1.14
git clone https://github.com/salesforce/ctrl
pip show tensorflow_estimator
(echo "import os" ; echo "print(os.listdir('${root}/CTRL Project_36 Layers/venv/lib/python3.6/site-packages/tensorflow_estimator/python/estimator/'))") | python
cd ./ctrl
patch -b ${root}/CTRL\ Project_36\ Layers/venv/lib/python3.6/site-packages/tensorflow_estimator/python/estimator/keras.py estimator.patch
pip install fastBPE
pip install gsutil
gsutil -m cp -r gs://sf-ctrl/seqlen256_36layers_v0.ckpt/ .
