from requests_folder.post_submit_an_order import post_submit_an_order


class Test_Post_Submit_Order:
    def test_post_submit_an_order(self):
        # apelam metoda submit si ii dam parametrii
        response = post_submit_an_order(1, "John")
        # s-a generat un rezultat care s-a salvat in response
        # Verificam urmatoarele:
        # order creation : True
        # status code trebuie sa fie 201
        # orer id lenght > 0
        assert response.json()[
                   'created'] == True, f"Error: Order creation status is not corect. EXPECTED: True, Actual:{response.json()['created']}"
        assert response.status_code == 201, f"Error: Status code is not valid. EXPECTED : 201, ACTUAL: {response.status_code}"
        assert len(response.json()[
                       'orderId']) > 0, f"Error: Order id is invalid. EXPECTED: len > 0, ACTUAL: {len(response.json()['orderId'])}"
