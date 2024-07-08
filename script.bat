@echo off
python3 -m venv venv
call .\venv\Scripts\activate
pip install tk pyautogui
python da.py
close