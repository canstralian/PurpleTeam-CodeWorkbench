import unittest

from utils.models import EvidenceEntry, Finding, ScopeRecord
from utils.reporting import build_report_markdown


class TestReporting(unittest.TestCase):
    def test_build_report_markdown_no_scope(self) -> None:
        self.assertEqual(build_report_markdown(None, [], []), "# Purple Team Report\n\nNo scope defined.\n")

    def test_build_report_markdown_success(self) -> None:
        scope = ScopeRecord(
            engagement_name="Eng",
            target_system="Sys",
            authorization_owner="Owner",
            start_date="2026-05-17",
            end_date="2026-05-18",
            allowed_actions=["Action"],
            constraints="Cons",
            authorization_confirmed=True,
            created_at="now"
        )
        finding = Finding(
            finding_id="F1", title="T1", severity="S1", confidence="C1",
            status="D", affected_asset="A", summary="S", evidence="E",
            impact="I", remediation="R", validation_notes="V", created_at="now"
        )
        evidence = EvidenceEntry(
            entry_id="E1", category="C", description="D", source="S",
            previous_hash="PH", entry_hash="EH", created_at="now"
        )

        md = build_report_markdown(scope, [finding], [evidence])
        self.assertIn("# Purple Team Security Workflow Report", md)
        self.assertIn("**Engagement:** Eng", md)
        self.assertIn("F1: T1", md)
        self.assertIn("E1: C", md)

if __name__ == "__main__":
    unittest.main()
