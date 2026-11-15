#!/usr/bin/env python3
import unittest
import os
import json

# Import modules from root directory for testing
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fim import calculate_sha256
from hash_auditor import compute_hashes

class TestSOCToolkit(unittest.TestCase):
    
    def test_sha256_missing_file(self):
        """Test that FIM gracefully returns None for non-existent files."""
        result = calculate_sha256("nonexistent_security_file_999.py")
        self.assertIsNone(result)

    def test_baseline_storage_workflow(self):
        """Test JSON baseline serialization for file integrity monitoring."""
        test_store = "test_baseline.json"
        mock_baseline = {"core_module.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
        
        with open(test_store, "w") as f:
            json.dump(mock_baseline, f)
            
        self.assertTrue(os.path.exists(test_store))
        
        with open(test_store, "r") as f:
            data = json.load(f)
            
        self.assertIn("core_module.py", data)
        self.assertEqual(len(data["core_module.py"]), 64) # SHA-256 hex length
        
        # Clean up test artifact
        os.remove(test_store)

if __name__ == "__main__":
    unittest.main()
