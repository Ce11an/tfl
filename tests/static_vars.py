"""Static variables for testing."""

LIFT_DISRUPTIONS = [
    {
        "stationUniqueId": "910GSHENFLD",
        "disruptedLiftUniqueIds": ["910GSHENFLD-Lift-1"],
        "message": "Shenfield: No Step Free Access - Step-free access is "
        "not available to the Greater Anglia platforms 3 and 4 and the Elizabeth "
        "line platforms 5 and 6 due to faulty lifts. Call us on 0343 222 1234 if you"
        "need help planning your journey.",
    },
    {
        "stationUniqueId": "910GTAPLOW",
        "disruptedLiftUniqueIds": ["910GTAPLOW-Lift-1"],
        "message": "Taplow: No Step Free Access - Step free access is not "
        "available between the entrance on Bath Road and the footbridge. For step "
        "free access, use the entrance on Approach Road. Call 0343 222 1234 if you "
        "need help planning your journey.",
    },
]


ACCIDENT_STATS_BEFORE_2020 = [
    {
        "$type": "Tfl.Api.Presentation.Entities.AccidentStats.AccidentDetail, Tfl.Api.Presentation.Entities",
        "id": 345979,
        "lat": 51.570865,
        "lon": -0.231959,
        "location": "On Edgware Road Near The Junction With north Circular Road",
        "date": "2019-01-04T21:22:00Z",
        "severity": "Slight",
        "borough": "Barnet",
        "casualties": [
            {
                "$type": "Tfl.Api.Presentation.Entities.AccidentStats.Casualty, Tfl.Api.Presentation.Entities",
                "age": 20,
                "class": "Driver",
                "severity": "Slight",
                "mode": "PoweredTwoWheeler",
                "ageBand": "Adult",
            }
        ],
        "vehicles": [
            {
                "$type": "Tfl.Api.Presentation.Entities.AccidentStats.Vehicle, Tfl.Api.Presentation.Entities",
                "type": "Motorcycle_500cc_Plus",
            }
        ],
    }
]

ACCIDENT_STATS_AFTER_2020 = {
    "$type": "Tfl.Api.Presentation.Entities.ApiError, Tfl.Api.Presentation.Entities",
    "timestampUtc": "2023-05-07T19:47:44.7682155Z",
    "exceptionType": "ApiArgumentException",
    "httpStatusCode": 400,
    "httpStatus": "BadRequest",
    "relativeUri": "/AccidentStats/2020",
    "message": "The following year is not recognised: 2020",
}
