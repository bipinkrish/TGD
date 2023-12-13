@echo off
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --noconfirm --onefile --console tgd.py
move dist\tgd.exe tgd.exe
rmdir /s /q build dist
del tgd.spec
