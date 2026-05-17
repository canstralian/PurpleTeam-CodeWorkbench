import unittest
from unittest.mock import MagicMock, patch

from utils.helpers import scope_is_unlocked
from utils.models import ScopeRecord


class TestHelpers(unittest.TestCase):
    @patch("streamlit.session_state")
    def test_scope_is_unlocked_false_empty(self, mock_session_state: MagicMock) -> None:
        mock_session_state.scope = None
        self.assertFalse(scope_is_unlocked())

    @patch("streamlit.session_state")
    def test_scope_is_unlocked_false_unconfirmed(self, mock_session_state: MagicMock) -> None:
        mock_session_state.scope = ScopeRecord(
            engagement_name="Test",
            target_system="Target",
            authorization_owner="Owner",
            start_date="2026-05-17",
            end_date="2026-05-18",
            allowed_actions=[],
            constraints="",
            authorization_confirmed=False,
            created_at="now"
        )
        self.assertFalse(scope_is_unlocked())

    @patch("streamlit.session_state")
    def test_scope_is_unlocked_true(self, mock_session_state: MagicMock) -> None:
        mock_session_state.scope = ScopeRecord(
            engagement_name="Test",
            target_system="Target",
            authorization_owner="Owner",
            start_date="2026-05-17",
            end_date="2026-05-18",
            allowed_actions=[],
            constraints="",
            authorization_confirmed=True,
            created_at="now"
        )
        self.assertTrue(scope_is_unlocked())

if __name__ == "__main__":
    unittest.main()
