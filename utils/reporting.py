
from utils.export import render_findings_markdown
from utils.models import EvidenceEntry, Finding, ScopeRecord


def build_report_markdown(
    scope: ScopeRecord | None,
    findings: list[Finding],
    evidence: list[EvidenceEntry]
) -> str:
    """Build a Markdown report from scope, findings, and evidence."""

    if not scope:
        return "# Purple Team Report\n\nNo scope defined.\n"

    report = [
        "# Purple Team Security Workflow Report",
        "",
        "## Engagement Scope",
        "",
        f"- **Engagement:** {scope.engagement_name}",
        f"- **Target/System:** {scope.target_system}",
        f"- **Authorization owner:** {scope.authorization_owner or 'Not specified'}",
        f"- **Date range:** {scope.start_date} to {scope.end_date}",
        f"- **Created:** {scope.created_at}",
        "",
        "### Allowed Actions",
        "",
        *[f"- {action}" for action in scope.allowed_actions],
        "",
        "### Constraints",
        "",
        scope.constraints or "No additional constraints recorded.",
        "",
        "## Executive Summary",
        "",
        (
            f"This report contains {len(findings)} finding(s) and "
            f"{len(evidence)} evidence ledger entrie(s). All outputs require "
            "human validation before operational use."
        ),
        "",
        "## Findings",
        "",
    ]

    if findings:
        report.append(render_findings_markdown(findings))
    else:
        report.append("No findings recorded.")

    report.extend(
        [
            "",
            "## Evidence Ledger Summary",
            "",
        ]
    )

    if evidence:
        for entry in evidence:
            report.extend(
                [
                    f"### {entry.entry_id}: {entry.category}",
                    "",
                    f"- **Source:** {entry.source or 'Not specified'}",
                    f"- **Created:** {entry.created_at}",
                    f"- **Previous hash:** `{entry.previous_hash}`",
                    f"- **Entry hash:** `{entry.entry_hash}`",
                    "",
                    entry.description,
                    "",
                ]
            )
    else:
        report.append("No evidence entries recorded.")

    report.extend(
        [
            "",
            "## Human Review Checklist",
            "",
            "- Scope matches written authorization.",
            "- Findings are supported by evidence.",
            "- Remediation advice is realistic and non-destructive.",
            "- Generated material was reviewed before use.",
            "- No unscoped targets or unsafe actions are included.",
        ]
    )

    return "\n".join(report)
