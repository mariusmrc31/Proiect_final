from requests_folder.get_a_single_book import get_a_single_book


class TestGetASingleBook:
    def test_get_a_single_book(self):
        response = get_a_single_book(1)
        assert response.status_code == 200, f"ERROR: status code is not correct. EXPECTED: 200. ACTUAL:{response.status_code}"
