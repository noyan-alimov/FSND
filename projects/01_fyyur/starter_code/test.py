from app import Venue

venues = Venue.query.all()
cities = []
for venue in venues:
    city = venue.city
    cities.append(city)

print(cities)
