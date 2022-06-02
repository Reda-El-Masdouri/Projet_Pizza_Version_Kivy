from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://jrpizzamamadjango2.herokuapp.com/api/GetPizzas"

        def data_recieved(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i["fields"])
            print(pizzas_dict)
            if on_complete:
                on_complete(pizzas_dict)
        def data_error(req, error):
            print("data_error: "+ str(error))
            if on_error:
                on_error(str(error))
        def date_failure(req, result):
            print("data_failure")
            if on_error:
                on_error("ERREUR SERVEUR: "+ str(req.resp_status))

        req = UrlRequest(url, on_success=data_recieved, on_error=data_error, on_failure=date_failure)