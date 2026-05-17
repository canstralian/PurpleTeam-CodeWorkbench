"""
utils/models.py
Data models and shared constants for the Purple Team Code Workbench.
"""

from dataclasses import dataclass

APP_TITLE = "Purple Team Code Workbench"
APP_SUBTITLE = (
    "Scope-gated workflow surface for authorized purple-team security work."
)

@dataclass
class ScopeRecord:
    """Represents the explicit authorization boundary for the session."""
    engagement_name: str
    target_system: str
    authorization_owner: str
    start_date: str
    end_date: str
    allowed_actions: list[str]
    constraints: str
    authorization_confirmed: bool
    created_at: str

@dataclass
class Finding:
    """Represents a structured security finding."""
    finding_id: str
    title: str
    severity: str
    confidence: str
    status: str
    affected_asset: str
    summary: str
    evidence: str
    impact: str
    remediation: str
    validation_notes: str
    created_at: str

@dataclass
class EvidenceEntry:
    """Represents an append-only evidence ledger entry."""
    entry_id: str
    category: str
    description: str
    source: str
    previous_hash: str
    entry_hash: str
    created_at: str

MODEL_ROLES: dict[str, str] = {
    "DeepHat/DeepHat-V1-7B": "Security-oriented generation workflows",
    "HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive": (
        "Experimental coding and reasoning"
    ),
    "meta-llama/Meta-Llama-3-8B-Instruct": (
        "General reasoning and structured instruction following"
    ),
}

ALLOWED_ACTIONS = [
    "Passive reconnaissance planning",
    "Detection engineering",
    "Finding classification",
    "Remediation planning",
    "Report drafting",
    "Safe proof-of-concept pseudocode",
    "Log analysis",
    "Control validation",
]

DISALLOWED_ACTIONS = [
    "Credential theft",
    "Persistence tooling",
    "Malware deployment",
    "Unauthorized exploitation",
    "Destructive testing",
    "Autonomous offensive execution",
    "Unscoped target interaction",
]
