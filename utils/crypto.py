import hashlib
import json


def compute_entry_hash(
    entry_id: str,
    category: str,
    description: str,
    source: str,
    previous_hash: str,
    created_at: str,
) -> str:
    """Compute a SHA-256 hash for an evidence ledger entry."""

    payload = {
        "entry_id": entry_id,
        "category": category,
        "description": description,
        "source": source,
        "previous_hash": previous_hash,
        "created_at": created_at,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
