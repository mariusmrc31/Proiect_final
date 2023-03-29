from requests_folder.delete_an_order import delete_an_order
from requests_folder.post_submit_an_order import post_submit_an_order


class TestDeleteAnOrder:
    def test_delete_an_order(self):
        submit = post_submit_an_order(4, "Emi")
        order_id = submit.json()["orderId"]
        response = delete_an_order(order_id)
        assert response.status_code == 204, f"Error: Status code este invalid. Expected: 204, Actual:{response.status_code}"
