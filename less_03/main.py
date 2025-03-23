# class GIS:
#     latitude = 55.23342342
#     longitude = 53.45454
#     name = "Office Ozon"
#     photo = "https://example.photo.jpg"

class GIS:
    def __init__(self, latitude, longitude, name, photo):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.photo = photo

    def show_info(self):
        msg_template = "Координаты: {lat} {lon}. Имя: {name}. Фото: {photo}"
        return msg_template.format(
            lat=self.latitude,
            lon=self.longitude,
            name=self.name,
            photo=self.photo,
        )


class GasStation(GIS):
    def __init__(
        self,
        count_of_trk,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.count_of_trk = count_of_trk

    def show_info(self):
        info = super().show_info()
        return info + f" Количество трк: {self.count_of_trk}"


print('*'*10)


# office = GIS(latitude=55.233232, longitude=52.3242342, name="Office Ozon", photo="https://exm.photo.jpg")
# office = GIS(55.233232, 52.3242342, "Office Ozon", "https://exm.photo.jpg")
azs = GasStation(5, 52.45454, 53.12131, "AZS", "photolink")


print(
    azs.show_info()
)


print('*'*10)

import request


class HttpClientGasStation():
    def __init__(self, base_url, api_key):
        ...
    
    def get_default_headers(self):
        ...
    
    
    def station_info(self):
        response = self.session.get('...')
        return response
    