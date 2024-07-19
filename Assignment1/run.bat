@echo off
setlocal

echo Checking if Python is installed...
REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

REM Check if the virtual environment already exists
if exist venv (
    echo Virtual environment already exists.
) else (
    echo Creating a virtual environment...
    REM Create a virtual environment
    python -m venv venv
)

echo Activating the virtual environment...
REM Activate the virtual environment
call venv\Scripts\activate

echo Installing required libraries...
REM Install the required library
pip install tk

echo Setting PYTHONPATH to include the src directory...
REM Set PYTHONPATH to include the src directory
set PYTHONPATH=%CD%\src

echo Running the main application...
REM Run the main application as a module
python -m src.main

echo Deactivating the virtual environment...
REM Deactivate the virtual environment
deactivate

echo Done.
endlocal
pause
