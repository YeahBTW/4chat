#!/bin/sh
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
cp .tagging.py env/lib/python*/site-packages/chatterbot/tagging.py
deactivate