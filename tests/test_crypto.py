import unittest

from utils.crypto import compute_entry_hash


class TestCrypto(unittest.TestCase):
    def test_compute_entry_hash(self) -> None:
        entry_id = "EVD-001"
        category = "Observation"
        description = "Test description"
        source = "Test source"
        previous_hash = "GENESIS"
        created_at = "2026-05-17T12:00:00Z"

        hash_val = compute_entry_hash(
            entry_id, category, description, source, previous_hash, created_at
        )

        self.assertIsInstance(hash_val, str)
        self.assertEqual(len(hash_val), 64) # SHA-256 length

if __name__ == "__main__":
    unittest.main()
