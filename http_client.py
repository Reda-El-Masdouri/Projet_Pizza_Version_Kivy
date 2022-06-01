from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:
    def get_pizzas(self, on_complete):
        url = "https://jrpizzamamadjango2.herokuapp.com/api/GetPizzas"

        def data_recieved(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i["fields"])
            print(pizzas_dict)
            if on_complete:
                on_complete(pizzas_dict)

        req = UrlRequest(url, on_success=data_recieved)