# How to Fix Pylance Type Issues in Your Project

## The Problem
When using `singleton_decorator` in your Python project, you see this error:
```
Expected class but received "_SingletonWrapper" PylancereportGeneralTypeIssues
```

## The Solution

### Step 1: Install the type stubs package

In your project directory, install the type stubs:

Using pip:
```bash
pip install types-singleton-decorator
```

Using uv:
```bash
uv add types-singleton-decorator
```

Using poetry:
```bash
poetry add types-singleton-decorator
```

### Step 2: Restart your language server

In VS Code:
1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Python: Restart Language Server"
3. Press Enter

### Step 3: Verify the fix

Your singleton classes should now have proper type support:

```python
from singleton_decorator import singleton

@singleton
class DatabaseConnection:  # ✅ No more type errors
    def __init__(self, host: str, port: int = 5432):
        self.host = host
        self.port = port
    
    def connect(self) -> bool:
        return True

# This will now have proper typing
db = DatabaseConnection("localhost")  # Type: DatabaseConnection
result = db.connect()                  # Type: bool
```

## What This Fixes

- ✅ Pylance recognizes decorated classes as proper classes
- ✅ Autocomplete works for class methods and attributes  
- ✅ Type checking works correctly
- ✅ No more "_SingletonWrapper" type errors
- ✅ mypy compatibility

## Troubleshooting

**Still seeing errors?**
1. Make sure `types-singleton-decorator` is installed in the same Python environment as your project
2. Restart VS Code completely
3. Check your Python interpreter selection in VS Code
4. Verify the package is installed: `pip list | grep types-singleton`

**For teams:**
Add `types-singleton-decorator` to your `requirements.txt`, `pyproject.toml`, or dependency management file so all team members get the type stubs automatically.

## Alternative: Local Type Stubs

If you prefer not to install a separate package, you can create local type stubs in your project:

1. Create a `stubs/singleton_decorator/__init__.pyi` file in your project
2. Copy the contents from this package's stub file
3. Add the stubs directory to your Python path or use mypy configuration
