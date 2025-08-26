@echo off
set APP=Test_Project_AI_agent.py
if exist %APP% (
    streamlit run %APP%
) else (
    echo Файл %APP% не найден!
)
pause
