# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
if (Test-Path -Path "./venv/Scripts/Activate.ps1") {
    . .\venv\Scripts\Activate.ps1
} else {
    Write-Error "Activation script not found. Ensure the virtual environment setup is correct."
    exit 1
}


