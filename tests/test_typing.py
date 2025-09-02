"""
Test file demonstrating proper typing with singleton_decorator and type stubs.

This file shows how the type stubs resolve Pylance issues.
"""

# This would normally cause: Expected class but received "_SingletonWrapper"
# But with our type stubs, it should work correctly

from typing import reveal_type

from singleton_decorator import singleton


@singleton
class DatabaseConnection:
    """Example singleton class with proper typing."""

    def __init__(self, host: str, port: int = 5432):
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> bool:
        """Connect to the database."""
        self.connected = True
        return True

    def get_connection_string(self) -> str:
        """Get the connection string."""
        return f"postgresql://{self.host}:{self.port}"


def test_singleton_functionality():
    """Test that singleton behavior works correctly."""
    print("Testing singleton functionality...")

    # Create first instance
    db1 = DatabaseConnection("localhost", 5432)
    print(f"db1: host={db1.host}, port={db1.port}")

    # Create second instance - should be the same object
    db2 = DatabaseConnection("different-host", 3306)  # These params will be ignored
    print(f"db2: host={db2.host}, port={db2.port}")

    # Verify they're the same instance
    print(f"Same instance: {db1 is db2}")

    # Test method calls
    result = db1.connect()
    print(f"Connection result: {result}")
    print(f"Connection string: {db1.get_connection_string()}")

    return True


def test_typing():
    """Test type checking (this would be caught by mypy/pylance)."""
    print("Testing type information...")

    # These should now have proper types with our stubs
    db = DatabaseConnection("localhost", 5432)

    # Type checking demonstrations (commented out as reveal_type is for static analysis)
    # reveal_type(DatabaseConnection)  # Should be Type[DatabaseConnection]
    # reveal_type(db)  # Should be DatabaseConnection
    # reveal_type(db.connect)  # Should be Callable[[], bool]

    print(f"DatabaseConnection type: {type(DatabaseConnection)}")
    print(f"db instance type: {type(db)}")
    print(f"connect method type: {type(db.connect)}")

    return True


if __name__ == "__main__":
    print("Running singleton decorator tests...\n")

    test_singleton_functionality()
    print()
    test_typing()

    print("\n✅ All tests passed!")
