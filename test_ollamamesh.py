# test_ollamamesh.py
"""
Tests for OllamaMesh module.
"""

import unittest
from ollamamesh import OllamaMesh

class TestOllamaMesh(unittest.TestCase):
    """Test cases for OllamaMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OllamaMesh()
        self.assertIsInstance(instance, OllamaMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OllamaMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
