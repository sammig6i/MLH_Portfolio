#!/bin/bash

source python3-virtualenv/bin/activate
pip install -r requirements.txt
python3 -m unittest discover -v tests/
