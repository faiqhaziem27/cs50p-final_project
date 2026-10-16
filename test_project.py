import pytest
from project import ContactManager

@pytest.fixture
def manager():
    return ContactManager()

def test_load_txt(manager, tmp_path):
    dummy_txt_file = tmp_path / "source_data.txt"
    dummy_txt_file.write_text("Name: John Doe. Email: john@cs50.edu Phone: +1 555-123-4567")

    manager.load_txt(str(dummy_txt_file))

    assert len(manager.contacts) == 1
    assert manager.contacts[0]["name"] == "John Doe"
    assert manager.contacts[0]["email"] == "john@cs50.edu"
    assert manager.contacts[0]["phone"] == "+1 555-123-4567"

def test_get_valid_contacts(manager):
    manager.contacts = [
        {"name": "Alice Vance", "email": "alice@harvard.edu", "phone": "+60123456789"},
        {"name": "N/A", "email": "Unknown", "phone": "N/A"},
        {"name": "Bob Miller", "email": "Unknown", "phone": "N/A"},
        {"name": "N/A", "email": "staff@site.com", "phone": "N/A"}
    ]

    clean_results = manager.get_valid_contacts

    assert len(clean_results) == 3
    assert {"name": "Alice Vance", "email": "alice@harvard.edu", "phone": "+60123456789"} in clean_results
    assert {"name": "N/A", "email": "Unknown", "phone": "N/A"} not in clean_results

def test_export_to_csv(manager, tmp_path):
    dummy_output_file = tmp_path / "exported_results.csv"

    assert manager.export_to_csv([], str(dummy_output_file)) is False

    mock_clean_rows = [
        {"name": "Charlie Green", "email": "charlie@domain.com", "phone": "+1234567890"}
    ]

    export_status = manager.export_to_csv(mock_clean_rows, str(dummy_output_file))

    assert export_status is True

    with open(dummy_output_file, "r") as f:
        file_content_lines = f.read().splitlines()
        assert file_content_lines[0] == "name,email,phone"
        assert file_content_lines[1] == "Charlie Green,charlie@domain.com,+1234567890"

