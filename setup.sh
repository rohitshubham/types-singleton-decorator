#!/bin/bash

# Development setup script for types-singleton-decorator

echo "Setting up development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install development dependencies
pip install --upgrade pip
pip install build twine mypy pylance-cli

echo "Setup complete!"
echo ""
echo "To build the package:"
echo "  python -m build"
echo ""
echo "To install locally for testing:"
echo "  pip install -e ."
echo ""
echo "To upload to PyPI (after configuring credentials):"
echo "  twine upload dist/*"
