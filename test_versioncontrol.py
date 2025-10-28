# test_versioncontrol.py
"""
Tests for VersionControl module.
"""

import unittest
from versioncontrol import VersionControl

class TestVersionControl(unittest.TestCase):
    """Test cases for VersionControl class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VersionControl()
        self.assertIsInstance(instance, VersionControl)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VersionControl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
