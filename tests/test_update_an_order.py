from requests_folder.post_submit_an_order import post_submit_an_order
from requests_folder.update_an_order import update_an_order


class TestUpdateAnOrder:
    def test_update_an_order(self):
        submit = post_submit_an_order(4, "Emi")
        order_id = submit.json()["orderId"]
        response = update_an_order("Marius", order_id)
        assert response.status_code == 204, f"Error: Status code is not valid. EXPECTED : 204, ACTUAL: {response.status_code}"
