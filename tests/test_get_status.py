from requests_folder.get_status import get_status


class TestGetStatus:
    def test_get_status(self):
        response = get_status()
        assert response.status_code == 200, f"Error: Status code is invalid. Expected: 200, Actual:{response.status_code}"
