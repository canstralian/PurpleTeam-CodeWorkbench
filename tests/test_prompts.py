import unittest

from prompts.engine import generate_workflow_prompt
from utils.models import ScopeRecord


class TestPrompts(unittest.TestCase):
    def test_generate_workflow_prompt(self) -> None:
        scope = ScopeRecord(
            engagement_name="Test Engagement",
            target_system="Test Target",
            authorization_owner="Test Owner",
            start_date="2026-05-17",
            end_date="2026-05-18",
            allowed_actions=["Log analysis"],
            constraints="No production",
            authorization_confirmed=True,
            created_at="2026-05-17T10:00:00Z"
        )

        prompt = generate_workflow_prompt(
            selected_model="DeepHat/DeepHat-V1-7B",
            scope=scope,
            workflow_type="Detection engineering plan",
            objective="Test objective",
            trusted_context="Trusted",
            untrusted_context="Untrusted",
            output_format="Markdown"
        )

        self.assertIn("AUTHORIZED SCOPE", prompt)
        self.assertIn("Test Engagement", prompt)
        self.assertIn("Detection engineering plan", prompt)
        self.assertIn("DeepHat/DeepHat-V1-7B", prompt)

    def test_generate_workflow_prompt_no_scope(self) -> None:
        prompt = generate_workflow_prompt(
            selected_model="DeepHat/DeepHat-V1-7B",
            scope=None,
            workflow_type="Detection engineering plan",
            objective="Test objective",
            trusted_context="Trusted",
            untrusted_context="Untrusted",
            output_format="Markdown"
        )
        self.assertIn("AUTHORIZED SCOPE\n{}", prompt)

    def test_generate_workflow_prompt_empty_context(self) -> None:
        prompt = generate_workflow_prompt(
            selected_model="DeepHat/DeepHat-V1-7B",
            scope=None,
            workflow_type="Detection engineering plan",
            objective="Test objective",
            trusted_context="",
            untrusted_context="",
            output_format="Markdown"
        )
        self.assertIn("No trusted context provided.", prompt)
        self.assertIn("No untrusted context provided.", prompt)

if __name__ == "__main__":
    unittest.main()
