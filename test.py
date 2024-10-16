# import datetime

# def convert_unix_to_datetime(unix_time):

#     normal_time = datetime.datetime.fromtimestamp(unix_time)
#     return normal_time.strftime('%d-%m-%Y %H:%M:%S')

# unix_time = 1697044800
# print("Normal time:", convert_unix_to_datetime(unix_time))


# just for not displaying error;
null = 0
false = 0

# ~ Aviationstack urls
#! url for flights
url = "https://api.aviationstack.com/v1/flights?access_key=5a2524c160cb81bd5cab9d67ee19f76c"

{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 1669022
    },
    "data": [
        {
            "flight_date": "2019-12-12",
            "flight_status": "active",
            "departure": {
                "airport": "San Francisco International",
                "timezone": "America/Los_Angeles",
                "iata": "SFO",
                "icao": "KSFO",
                "terminal": "2",
                "gate": "D11",
                "delay": 13,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": "2019-12-12T04:20:13+00:00",
                "estimated_runway": "2019-12-12T04:20:13+00:00",
                "actual_runway": "2019-12-12T04:20:13+00:00"
            },
            "arrival": {
                "airport": "Dallas/Fort Worth International",
                "timezone": "America/Chicago",
                "iata": "DFW",
                "icao": "KDFW",
                "terminal": "A",
                "gate": "A22",
                "baggage": "A17",
                "delay": 0,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": null,
                "estimated_runway": null,
                "actual_runway": null
            },
            "airline": {
                "name": "American Airlines",
                "iata": "AA",
                "icao": "AAL"
            },
            "flight": {
                "number": "1004",
                "iata": "AA1004",
                "icao": "AAL1004",
                "codeshared": null
            },
            "aircraft": {
               "registration": "N160AN",
               "iata": "A321",
               "icao": "A321",
               "icao24": "A0F1BB"
            },
            "live": {
                "updated": "2019-12-12T10:00:00+00:00",
                "latitude": 36.28560000,
                "longitude": -106.80700000,
                "altitude": 8846.820,
                "direction": 114.340,
                "speed_horizontal": 894.348,
                "speed_vertical": 1.188,
                "is_ground": false
            }
        }, 
        [...]
    ]
}


#! url for AIRPORTS
url = "https://api.aviationstack.com/v1/airports?access_key=5a2524c160cb81bd5cab9d67ee19f76c"

{
   "pagination": {
       "limit": 100,
       "offset": 0,
       "count": 100,
       "total": 6471
   },
   "data": [
      {
         "airport_name": "Anaa",
         "iata_code": "AAA",
         "icao_code": "NTGA",
         "latitude": "-17.05",
         "longitude": "-145.41667",
         "geoname_id": "6947726",
         "timezone": "Pacific/Tahiti",
         "gmt": "-10",
         "phone_number": null,
         "country_name": "French Polynesia",
         "country_iso2": "PF",
         "city_iata_code": "AAA"
      },
      [...]
   ]
}

#! url for AIRLINES
url = "https://api.aviationstack.com/v1/airlines?access_key=5a2524c160cb81bd5cab9d67ee19f76c"

{
   "pagination": {
       "limit": 100,
       "offset": 0,
       "count": 100,
       "total": 13131
   },
   "data": [
      {
         "airline_name": "American Airlines",
         "iata_code": "AA",
         "iata_prefix_accounting": "1",
         "icao_code": "AAL",
         "callsign": "AMERICAN",
         "type": "scheduled",
         "status": "active",
         "fleet_size": "963",
         "fleet_average_age": "10.9",
         "date_founded": "1934",
         "hub_code": "DFW",
         "country_name": "United States",
         "country_iso2": "US"
      },
      [...]
   ]
}

#! url for AIRPLANES
url = "https://api.aviationstack.com/v1/airplanes?access_key=5a2524c160cb81bd5cab9d67ee19f76c"

{
   "pagination": {
       "limit": 100,
       "offset": 0,
       "count": 100,
       "total": 19052
   },
   "data": [
      {
         "registration_number": "YR-BAC",
         "production_line": "Boeing 737 Classic",
         "iata_type": "B737-300",
         "model_name": "737",
         "model_code": "B737-377",
         "icao_code_hex": "4A0823",
         "iata_code_short": "B733",
         "construction_number": "23653",
         "test_registration_number": null,
         "rollout_date": null,
         "first_flight_date": "1986-08-02T22:00:00.000Z",
         "delivery_date": "1986-08-21T22:00:00.000Z",
         "registration_date": "0000-00-00",
         "line_number": "1260",
         "plane_series": "377",
         "airline_iata_code": "0B",
         "airline_icao_code": null,
         "plane_owner": "Airwork Flight Operations Ltd",
         "engines_count": "2",
         "engines_type": "JET",
         "plane_age": "31",
         "plane_status": "active",
         "plane_class": null
      },
      [...]
   ]
}

#! url for CITIES
url = "https://api.aviationstack.com/v1/cities?access_key=5a2524c160cb81bd5cab9d67ee19f76c"

{    
   "pagination": {
       "limit": 100,
       "offset": 0,
       "count": 100,
       "total": 9368
   },
   "data": [
      {
         "city_name": "Anaa",
         "iata_code": "AAA",
         "country_iso2": "PF",
         "latitude": "-17.05",
         "longitude": "-145.41667",
         "timezone": "Pacific/Tahiti",
         "gmt": "-10",
         "geoname_id": "0"
      },
      [...]
   ]
}

#! url for COUNTRIES
url = "https://api.aviationstack.com/v1/countries?access_key=5a2524c160cb81bd5cab9d67ee19f76c"

{
   "pagination": {
       "limit": 100,
       "offset": 0,
       "count": 100,
       "total": 252
   },
   "data": [
      {
         "country_name": "Andorra",
         "country_iso2": "AD",
         "country_iso3": "AND",
         "country_iso_numeric": "20",
         "population": "84000",
         "capital": "Andorra la Vella",
         "continent": "EU",
         "currency_name": "Euro",
         "currency_code": "EUR",
         "fips_code": "AN",
         "phone_prefix": "376"
      },
      [...]
   ]
}


