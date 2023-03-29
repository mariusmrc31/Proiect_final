from requests_folder.get_list_of_books import get_list_of_books


class Test_Get_List_Of_Books:
    def test_get_list_of_books_no_filter_check_response_status(self):
        response = get_list_of_books()
        assert response.status_code == 200, f"ERROR: status code is not correct. EXPECTED: 200. ACTUAL:{response.status_code}"

    def test_get_list_of_books_no_filter_check_number_of_results(self):
        response = get_list_of_books()
        assert len(response.json()) == 6, f"Error, EXPECTED: 6. ACTUAL: {len(response.json())}"

    def test_get_list_of_books_filter_non_fiction(self):
        response = get_list_of_books(type="non-fiction")
        assert response.status_code == 200, f"ERROR, EXPECTED: 200, ACTUAL: {response.status_code}"
        for i in response.json():
            assert i['type'] == "non-fiction", f"ERROR: EXPECTED: 'non-fiction', ACTUAL: {i['type']}"
