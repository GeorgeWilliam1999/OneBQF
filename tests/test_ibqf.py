"""
Unit tests for the IBQF implementation.

To run these tests:
    pytest tests/test_ibqf.py
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from ibqf import IBQF


class TestIBQF:
    """Test cases for the IBQF class."""
    
    def test_initialization(self):
        """Test that IBQF initializes correctly."""
        ibqf = IBQF(size=100, hash_functions=3)
        assert ibqf.size == 100
        assert ibqf.hash_functions == 3
        assert len(ibqf.filter) == 100
        assert all(bit == 0 for bit in ibqf.filter)
    
    def test_add_and_query(self):
        """Test adding items and querying them."""
        ibqf = IBQF(size=1000, hash_functions=3)
        
        # Add items
        items = ["track_1", "track_2", "track_3"]
        for item in items:
            ibqf.add(item)
        
        # Query added items - should all be True
        for item in items:
            assert ibqf.query(item) is True
    
    def test_query_non_existent(self):
        """Test querying items that were not added."""
        ibqf = IBQF(size=1000, hash_functions=3)
        
        # Add some items
        ibqf.add("track_1")
        ibqf.add("track_2")
        
        # Query non-existent item
        # Note: Due to false positives, this might return True
        # but we can't guarantee it returns False
        result = ibqf.query("track_99999")
        assert isinstance(result, bool)
    
    def test_reset(self):
        """Test resetting the filter."""
        ibqf = IBQF(size=100, hash_functions=3)
        
        # Add items
        ibqf.add("track_1")
        ibqf.add("track_2")
        
        # Reset
        ibqf.reset()
        
        # Filter should be all zeros
        assert all(bit == 0 for bit in ibqf.filter)
    
    def test_repr(self):
        """Test string representation."""
        ibqf = IBQF(size=100, hash_functions=3)
        repr_str = repr(ibqf)
        assert "IBQF" in repr_str
        assert "100" in repr_str
        assert "3" in repr_str


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
