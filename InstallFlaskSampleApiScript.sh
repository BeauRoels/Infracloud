#!/bin/bash

# Install dependancies
sudo apt-get install python3 python3-pip git

# Clone the repo
git clone https://github.com/nikolayg/sample-python-api.git
cd sample-python-api

# Create and execute the venv
python3 -m venv ./venv
. venv/bin/activate

# Install dependancies
pip install flask flask-restx pytest pytest-flask

# If flask-restplus still worked we could just run but nope, gotta swap this stuff to restx
sed -i 's/from flask_restplus/from flask_restx/g' src/*/*.py

# Run the damn program
python3 src/main.py