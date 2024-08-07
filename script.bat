@echo off
title "Script"
python3 -m venv venv
echo "Made Venv"
call .\venv\Scripts\activate
echo "Install libraries"
pip install tk pyautogui
python da.py
close
