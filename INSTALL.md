# Installation and Usage Guide

## Quick Start

### 1. Install the type stubs package

Using pip:
```bash
pip install types-singleton-decorator
```

Using uv:
```bash
uv add types-singleton-decorator
```

This will automatically install `singleton_decorator` as well.

### 2. No additional configuration needed

Once installed, Pylance and other type checkers will automatically pick up the type stubs.

## Fixing Your Project

### Before (with type errors):
```python
from singleton_decorator import singleton

@singleton
class MyService:  # Error: Expected class but received "_SingletonWrapper"
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

service = MyService("test")  # Pylance doesn't understand this is MyService
```

### After (with type stubs):
```python
from singleton_decorator import singleton

@singleton
class MyService:  # ✅ No error, properly typed as Type[MyService]
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

service = MyService("test")  # ✅ Properly typed as MyService
print(service.get_name())    # ✅ Method completion and type checking work
```

## Supported Patterns

The type stubs support all common singleton_decorator usage patterns:

### 1. Basic decorator
```python
@singleton
class MyClass:
    pass
```

### 2. Decorator with parentheses
```python
@singleton()
class MyClass:
    pass
```

### 3. Metaclass usage (if supported by singleton_wrapper)
```python
class MyClass(metaclass=SingletonMeta):
    pass
```

## Verification

To verify the type stubs are working:

1. Install the package in your project
2. Open your Python files using singleton_decorator in VS Code
3. Check that Pylance no longer shows type errors
4. Verify autocomplete works for your singleton classes

## Troubleshooting

If you're still seeing type errors:

1. Restart your language server (Cmd+Shift+P → "Python: Restart Language Server")
2. Check that `types-singleton-decorator` is installed in the same environment as your project
3. Verify your project is using the correct Python interpreter

## Development

To contribute or modify these type stubs:

1. Clone this repository
2. Make changes to `singleton_decorator-stubs/__init__.pyi`
3. Test with your project
4. Submit a pull request
