#! /usr/bin/env bash

pip3 install -r requirements.txt
pip3 install pyinstaller
pyinstaller --noconfirm --onefile --console tgd.py
mv dist/tgd tgd
chmod 777 tgd
rm -r build/ dist/ tgd.spec
