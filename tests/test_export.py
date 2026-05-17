import unittest

from utils.export import records_to_csv, render_findings_markdown
from utils.models import Finding


class TestExport(unittest.TestCase):
    def test_records_to_csv_empty(self) -> None:
        self.assertEqual(records_to_csv([]), "")

    def test_records_to_csv_success(self) -> None:
        records = [{"id": "1", "val": "a"}, {"id": "2", "val": "b"}]
        csv_out = records_to_csv(records)
        self.assertIn("id,val", csv_out)
        self.assertIn("1,a", csv_out)
        self.assertIn("2,b", csv_out)

    def test_render_findings_markdown_empty(self) -> None:
        self.assertEqual(render_findings_markdown([]), "# Findings\n")

    def test_render_findings_markdown_success(self) -> None:
        finding = Finding(
            finding_id="FIND-001",
            title="Test Finding",
            severity="High",
            confidence="High",
            status="Draft",
            affected_asset="Server",
            summary="Summary text",
            evidence="Evidence text",
            impact="Impact text",
            remediation="Remediation text",
            validation_notes="Validation text",
            created_at="now"
        )
        md = render_findings_markdown([finding])
        self.assertIn("FIND-001: Test Finding", md)
        self.assertIn("Summary text", md)

if __name__ == "__main__":
    unittest.main()
