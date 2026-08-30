# ⚡ Thesis Writer Kit - 1-Click Turnkey Installer (Windows)
# Usage: .\setup.ps1

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   THESIS WRITER KIT: 1-CLICK AUTOMATED SETUP" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Check Python
Write-Host "[1/4] Checking Python environment..." -ForegroundColor Yellow
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python 3.10+ is required but not found in PATH." -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/ and check 'Add Python to PATH'."
    exit 1
}

$pyVer = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
Write-Host "  ✓ Found Python $pyVer" -ForegroundColor Green

# Install Python requirements
Write-Host "  Installing Python engine dependencies..." -ForegroundColor Gray
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r .agent/opendraft/requirements.txt
Write-Host "  ✓ Python dependencies installed." -ForegroundColor Green

# 2. Check Node.js (Optional for Detector & Web UI)
Write-Host ""
Write-Host "[2/4] Checking Node.js environment..." -ForegroundColor Yellow
if (Get-Command node -ErrorAction SilentlyContinue) {
    $nodeVer = node -v
    Write-Host "  ✓ Found Node.js $nodeVer" -ForegroundColor Green
    if (Test-Path "tools/yourwrite/package.json") {
        Write-Host "  Installing YourWrite Web UI dependencies..." -ForegroundColor Gray
        Push-Location "tools/yourwrite"
        npm install --silent 2>$null
        Pop-Location
        Write-Host "  ✓ Web UI dependencies installed." -ForegroundColor Green
    }
} else {
    Write-Host "  ! Node.js not detected (optional for Web UI, CLI works with Python)." -ForegroundColor DarkGray
}

# 3. Setup Gemini API Key
Write-Host ""
Write-Host "[3/4] Configuring API Key..." -ForegroundColor Yellow
if ($env:GOOGLE_API_KEY) {
    Write-Host "  ✓ GOOGLE_API_KEY environment variable detected." -ForegroundColor Green
} else {
    $configEnv = ".agent/opendraft/engine/.env"
    if (Test-Path $configEnv) {
        Write-Host "  ✓ Found existing .env file in engine." -ForegroundColor Green
    } else {
        Write-Host "  ! No API key detected. Let's configure one (Free Gemini API Key):" -ForegroundColor Cyan
        $apiKey = Read-Host "  Enter your Google Gemini API Key (or press Enter to skip)"
        if ($apiKey) {
            "GOOGLE_API_KEY=$apiKey" | Out-File -FilePath $configEnv -Encoding utf8
            Write-Host "  ✓ Saved API key to $configEnv" -ForegroundColor Green
        }
    }
}

# 4. System Verification
Write-Host ""
Write-Host "[4/4] Verifying installation..." -ForegroundColor Yellow
Push-Location ".agent/opendraft/engine"
python -m opendraft.cli verify
Pop-Location

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "  🎉 SETUP COMPLETE! YOU ARE READY TO WRITE YOUR THESIS." -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Quick Commands:" -ForegroundColor Cyan
Write-Host "  1. Start Interactive Wizard:  cd .agent/opendraft/engine; python -m opendraft.cli"
Write-Host "  2. Audit AI Tells (0-100):    cd .agent/opendraft/engine; python -m opendraft.cli audit --text 'text...'"
Write-Host "  3. Humanize & Match Voice:    cd .agent/opendraft/engine; python -m opendraft.cli humanize --text 'text...' --sample sample.txt"
Write-Host "  4. Launch Web UI:             cd tools/yourwrite; npm start"
Write-Host ""
