# https://quera.org/problemset/148637/

from typing import Iterable


class ItemWithStatus:
    def __init__(self, status) -> None:
        self._status = status

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_state: str) -> None:
        self._status = new_state


class Plane(ItemWithStatus):
    pass


class Band(ItemWithStatus):
    pass


class Airport:
    def __init__(self, plane_ids: Iterable[str], number_of_bands: int) -> None:
        self._id_to_plane = {plane_id: Plane('1') for plane_id in plane_ids}
        self._bands = [Band('FREE') for _ in range(number_of_bands)]

    def take_off(self, plane_id: str) -> str:
        plane = self._get_plane_or_add(plane_id)
        if self._is_any_band_free() and plane.status == '1':
            plane.status = '2'
            free_band = self._find_first_free_band()
            free_band.status = plane_id
            return

        if plane.status == '1':
            return 'NO FREE BOUND'
        elif plane.status == '2':
            return 'YOU ARE TAKING OFF'
        elif plane.status == '3':
            return 'YOU ARE LANDING NOW'
        elif plane.status == '4':
            return 'YOU ARE NOT HERE'

    def landing(self, plane_id: str) -> str:
        plane = self._get_plane_or_add(plane_id)
        if self._is_any_band_free() and plane.status == '4':
            plane.status = '3'
            free_band = self._find_last_free_band()
            free_band.status = plane_id
            return

        if plane.status == '1':
            return 'YOU ARE HERE'
        elif plane.status == '2':
            return 'YOU ARE TAKING OFF'
        elif plane.status == '3':
            return 'YOU ARE LANDING NOW'
        elif plane.status == '4':
            return 'NO FREE BOUND'

    def plane_status(self, plane_id: str) -> str:
        plane = self._get_plane_or_add(plane_id)
        return plane.status

    def band_status(self, band_number: str) -> str:
        return self._bands[int(band_number) - 1].status

    def _get_plane_or_add(self, plane_id: str) -> Plane:
        if plane_id in self._id_to_plane:
            return self._id_to_plane[plane_id]
        new_plane = Plane('4')
        self._id_to_plane[plane_id] = new_plane
        return new_plane

    def _is_any_band_free(self) -> bool:
        return any(band.status == 'FREE' for band in self._bands)
    
    def _find_first_free_band(self) -> Band:
        for band in self._bands:
            if band.status == 'FREE':
                return band

    def _find_last_free_band(self) -> Band:
        for band in self._bands[::-1]:
            if band.status == 'FREE':
                return band


def main(
    number_of_bands: int,
    plane_ids: Iterable[str],
    orders: Iterable[str]
) -> None:
    airport = Airport(plane_ids, number_of_bands)
    result = []
    for order in orders:
        order_code, order_input = order.split(' ')
        if order_code == 'TAKE-OFF':
            result.append(airport.take_off(order_input))
        elif order_code == 'LANDING':
            result.append(airport.landing(order_input))
        elif order_code == 'PLANE-STATUS':
            result.append(airport.plane_status(order_input))
        elif order_code == 'BAND-STATUS':
            result.append(airport.band_status(order_input))
    return result


def get_input() -> None:
    number_of_planes, number_of_bands = map(int, input().split(' '))
    plane_ids = []
    for _ in range(number_of_planes):
        plane_ids.append(input())

    number_of_orders = int(input())
    orders = []
    for _ in range(number_of_orders):
        orders.append(input())
    return number_of_bands, plane_ids, orders


def print_results(results: Iterable[str]) -> None:
    for result in results:
        if result is not None:
            print(result)


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(main(*get_input()))
