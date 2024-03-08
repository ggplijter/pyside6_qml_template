# get root folder in trunk
$ROOT_FOLDER = Resolve-Path -Path  "$PSScriptRoot\..\"
Set-Location $ROOT_FOLDER

$PYTHON_VENV_EXE = "$ROOT_FOLDER\.venv\Scripts\python.exe"

& $PYTHON_VENV_EXE "$ROOT_FOLDER\main.py"
