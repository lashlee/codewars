#!/bin/bash
echo "Creating challenge file"
touch $1.py
echo "Creating test file"
cp ~/project/codewars/python/test_template.py test_$1.py

