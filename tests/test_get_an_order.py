from requests_folder.get_an_order import get_an_order
from requests_folder.post_submit_an_order import post_submit_an_order


class TestGetAnOrder:
    def test_get_an_order(self):
        submit = post_submit_an_order(4, "Emi")
        order_id = submit.json()["orderId"]
        response = get_an_order(order_id)
        assert response.status_code == 200, f"ERROR: status code is not correct. EXPECTED: 200. ACTUAL:{response.status_code}"
        assert response.json()["id"] == order_id, f" Order ids do not match. EXPECTED: {order_id}, ACTUAL: {response.json()['id']}"
