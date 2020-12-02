import requests


class Sheduler:
    def get_data(self, url, params, item):

        r = requests.get(url, params=params)
        try:
            json_data = r.json()
            data = json_data.get(item)
            if data:
                return {
                    "success": True,
                    "data": data,
                }

            else:
                return {
                    "success": False,
                    "data": [],
                }

        except Exception as e:
            return {
                "success": False,
                "message": repr(e),
            }

    def get_events(self, isSent):
        params = {"isSent": isSent}
        url = "https://programming-scheduler.herokuapp.com/lessons"
        data = self.get_data(url, params, "lessons")
        if data.get("success"):
            return data.get("data", [])

    def get_all_events(self):
        sent_events = self.get_events("true")
        unsent_events = self.get_events("false")
        return sent_events + unsent_events

    def get_default_events(self):
        params = {}
        url = "https://programming-scheduler.herokuapp.com/defaultLessons/"
        data = self.get_data(url, params, "lessons")
        if data.get("success"):
            return data.get("data", [])

    def get_images(self):
        experts = self.get_experts()
        url = "https://programming-scheduler.herokuapp.com/images/getImageByName"
        return [
            {
                "name": expert["name"],
                "image": str(
                    requests.get(
                        url,
                        params={"name": expert["name"]},
                    ).content,
                ),
            }
            for expert in experts
        ]
