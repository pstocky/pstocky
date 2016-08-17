#!/bin/bash

echo '>> iSort'
isort -rc -sp . .
echo

echo '>> PEP8'
pep8 --exclude=migrations --ignore=E128,E501 .
echo
