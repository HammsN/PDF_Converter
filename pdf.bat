@echo off
if "%1"=="--help" (
    echo %~nx0
    echo Description: Converts into .pdf format
    echo Usage: pdf ^<file_name.ext^>
    goto :eof
)

@call .venv\Scripts\activate.bat
@python pdf.py %*
@deactivate