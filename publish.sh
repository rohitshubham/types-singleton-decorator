#!/bin/bash

# Script to publish types-singleton-decorator to PyPI

set -e

echo "🔨 Building package..."
rm -rf dist/
python -m build

echo "📋 Checking package..."
twine check dist/*

echo "🔍 Contents of wheel:"
python -m zipfile -l dist/*.whl

echo "📦 Package built successfully!"
echo ""
echo "To upload to PyPI:"
echo "  1. Test upload: twine upload --repository testpypi dist/*"
echo "  2. Production: twine upload dist/*"
echo ""
echo "Note: Make sure you have configured your PyPI credentials:"
echo "  - Create account on pypi.org"
echo "  - Generate API token"
echo "  - Configure: pip install keyring; keyring set https://upload.pypi.org/legacy/ __token__"
