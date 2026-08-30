#!/usr/bin/env bash
# ⚡ Thesis Writer Kit - 1-Click Turnkey Installer (macOS & Linux)
# Usage: ./setup.sh

set -e

echo ""
echo "=========================================================="
echo "   THESIS WRITER KIT: 1-CLICK AUTOMATED SETUP"
echo "=========================================================="
echo ""

# 1. Check Python
echo "[1/4] Checking Python environment..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3.10+ is required but not found in PATH."
    exit 1
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "  ✓ Found Python $PY_VER"

echo "  Installing Python dependencies..."
python3 -m pip install --quiet --upgrade pip
python3 -m pip install --quiet -r .agent/opendraft/requirements.txt
echo "  ✓ Python dependencies installed."

# 2. Check Node.js
echo ""
echo "[2/4] Checking Node.js environment..."
if command -v node &> /dev/null; then
    NODE_VER=$(node -v)
    echo "  ✓ Found Node.js $NODE_VER"
    if [ -f "tools/yourwrite/package.json" ]; then
        echo "  Installing YourWrite Web UI dependencies..."
        (cd tools/yourwrite && npm install --silent)
        echo "  ✓ Web UI dependencies installed."
    fi
fi

# 3. Setup Gemini API Key
echo ""
echo "[3/4] Checking API Key..."
if [ -n "$GOOGLE_API_KEY" ]; then
    echo "  ✓ GOOGLE_API_KEY environment variable detected."
else
    CONFIG_ENV=".agent/opendraft/engine/.env"
    if [ -f "$CONFIG_ENV" ]; then
        echo "  ✓ Found existing .env file."
    else
        echo "  ! No API key detected. Free Gemini API Key configuration:"
        read -p "  Enter your Google Gemini API Key (or press Enter to skip): " API_KEY
        if [ -n "$API_KEY" ]; then
            echo "GOOGLE_API_KEY=$API_KEY" > "$CONFIG_ENV"
            echo "  ✓ Saved API key to $CONFIG_ENV"
        fi
    fi
fi

# 4. Verify
echo ""
echo "[4/4] Verifying installation..."
(cd .agent/opendraft/engine && python3 -m opendraft.cli verify)

echo ""
echo "=========================================================="
echo "  🎉 SETUP COMPLETE! YOU ARE READY TO WRITE YOUR THESIS."
echo "=========================================================="
echo ""
