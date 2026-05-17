import csv
import io
from typing import Any

from utils.models import Finding


def records_to_csv(records: list[dict[str, Any]]) -> str:
    """Convert records to a CSV string."""

    if not records:
        return ""

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)
    return buffer.getvalue()


def render_findings_markdown(findings: list[Finding]) -> str:
    """Render findings as Markdown."""

    sections = ["# Findings\n"]

    for finding in findings:
        sections.append(f"## {finding.finding_id}: {finding.title}\n")
        sections.append(f"- **Severity:** {finding.severity}")
        sections.append(f"- **Confidence:** {finding.confidence}")
        sections.append(f"- **Status:** {finding.status}")
        sections.append(f"- **Affected asset:** {finding.affected_asset or 'Not specified'}")
        sections.append(f"- **Created:** {finding.created_at}\n")
        sections.append("### Summary\n")
        sections.append(f"{finding.summary}\n")
        sections.append("### Evidence\n")
        sections.append(f"{finding.evidence or 'No evidence recorded.'}\n")
        sections.append("### Impact\n")
        sections.append(f"{finding.impact or 'No impact recorded.'}\n")
        sections.append("### Remediation\n")
        sections.append(f"{finding.remediation or 'No remediation recorded.'}\n")
        sections.append("### Validation Notes\n")
        sections.append(f"{finding.validation_notes or 'No validation notes recorded.'}\n")

    return "\n".join(sections)
