from consumers.db.models import Location
from consumers.settings.conection_postgresql import get_session


def get_location_by_lat_and_lon(latitude, longitude):
    with (get_session() as session):
        location = (session.query(Location)
                    .filter(Location.latitude == latitude, Location.longitude == longitude)
                    .first())
        return location


def insert_location(new_location: Location):
    with get_session() as session:
        location = get_location_by_lat_and_lon(new_location.latitude, new_location.longitude)
        if location:
            return
        session.add(new_location)
        session.commit()
