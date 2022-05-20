#!/bin/bash

sudo apt-get update && sudo apt-get install -y screen libfuzzy-dev python3.7 python3.7-venv libpython3.7-dev

/usr/bin/python3.7 -m pip install virtualenv
/usr/bin/python3.7 -m venv TRAIN

source TRAIN/bin/activate

pip install --upgrade pip
pip install wheel
pip install Cython

pip install -r requirements.txt

user=$(whoami)
dir_actual=$(pwd)
echo "source $dir_actual/TRAIN/bin/activate" >> /home/$user/.bashrc