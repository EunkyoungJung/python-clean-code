class Point:
    lat1: float
    long1: float

    def __init__(self, lat, long):
        self.lat: float = lat
        self.long: float = long


def locate(latitude: float, longitude: float) -> Point:
    """맵에서 좌표에 해당하는 객체를 검색"""


print(Point.__annotations__)
"""
{'lat': <class 'float'>, 'long': <class 'float'>}
"""
print(locate.__doc__)
"""
맵에서 좌표에 해당하는 객체를 검색
"""
print(locate.__annotations__)
"""
{'latitude': <class 'float'>, 'longitude': <class 'float'>, 'return': <class '__main__.Point'>}
"""