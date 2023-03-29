from requests_folder.get_all_orders import get_all_orders
from requests_folder.post_submit_an_order import post_submit_an_order


class TestGetAllOrders:
    def test_get_all_orders(self):
        post_submit_an_order(1, "John")
        # post_submit_an_order(7, "Tudor")
        post_submit_an_order(4, "Emi")
        response = get_all_orders()
        assert response.status_code == 200, f"Error: Status code is not valid. EXPECTED : 200, ACTUAL: {response.status_code}"
        assert len(response.json()) == 2, f"Error: lenght is not valid. EXPECTED: 2, ACTUAL: {len(response.json())}"
