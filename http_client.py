from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:
    def get_pizzas(self):
        url = "https://jrpizzamamadjango2.herokuapp.com/api/GetPizzas"

        def data_recieved(req, result):
            data = json.loads(result)
            pizzas_dict = [x["fields"] for x in data]
            print(pizzas_dict)

        req = UrlRequest(url, on_success=data_recieved)