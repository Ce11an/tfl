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

AIR_QUALITY = {
    "$id": "1",
    "$type": "Tfl.Api.Presentation.Entities.LondonAirForecast, Tfl.Api.Presentation.Entities",
    "updatePeriod": "hourly",
    "updateFrequency": "1",
    "forecastURL": "http://londonair.org.uk/forecast",
    "disclaimerText": "This forecast is intended to provide information on expected pollution levels in areas of "
    "significant public exposure. It may not apply in very specific locations close to unusually "
    "strong or short-lived local sources of pollution.",
    "currentForecast": [
        {
            "$id": "2",
            "$type": "Tfl.Api.Presentation.Entities.CurrentForecast, Tfl.Api.Presentation.Entities",
            "forecastType": "Current",
            "forecastID": "40578",
            "publishedDate": "2023-09-05T10:39:46Z",
            "fromDate": "2023-09-05T00:00:00Z",
            "toDate": "2023-11-05T23:59:00Z",
            "forecastBand": "Low",
            "forecastSummary": "Low air pollution forecast valid from Tuesday 9 May to end of Thursday 11 May GMT",
            "nO2Band": "Low",
            "o3Band": "Low",
            "pM10Band": "Low",
            "pM25Band": "Low",
            "sO2Band": "Low",
            "forecastText": "Sunny spells and scattered shower, potentially heavy and"
            " slow-moving.&lt;br/&gt;&lt;br/&gt;A "
            "&#39;clean&#39; westerly Atlantic air feed is expected, with a light breeze aiding dispersion "
            "of local emissions and minimal import. &lt;br/&gt;&lt;br/&gt;Air pollution is expected to "
            "remain in the &#39;Low&#39; banding throughout the forecast period for the following "
            "pollutants:&lt;br/&gt;&lt;br/&gt;Nitrogen dioxide&lt;br/&gt;Ozone&lt;br/&gt;PM2.5 "
            "Particulates&lt;br/&gt;PM10 Particulates&lt;br/&gt;Sulphur "
            "dioxide&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;",
        },
        {
            "$id": "3",
            "$type": "Tfl.Api.Presentation.Entities.CurrentForecast, Tfl.Api.Presentation.Entities",
            "forecastType": "Future",
            "forecastID": "40578",
            "publishedDate": "2023-09-05T10:39:46Z",
            "fromDate": "2023-09-05T00:00:00Z",
            "toDate": "2023-11-05T23:59:00Z",
            "forecastBand": "Low",
            "forecastSummary": "Low air pollution forecast valid from Tuesday 9 May to end of Thursday 11 May GMT",
            "nO2Band": "Low",
            "o3Band": "Low",
            "pM10Band": "Low",
            "pM25Band": "Low",
            "sO2Band": "Low",
            "forecastText": "Sunny spells and scattered shower, potentially heavy and "
            "slow-moving.&lt;br/&gt;&lt;br/&gt;A "
            "&#39;clean&#39; westerly Atlantic air feed is expected, with a light breeze aiding dispersion "
            "of local emissions and minimal import. &lt;br/&gt;&lt;br/&gt;Air pollution is expected to "
            "remain in the &#39;Low&#39; banding throughout the forecast period for the following "
            "pollutants:&lt;br/&gt;&lt;br/&gt;Nitrogen dioxide&lt;br/&gt;Ozone&lt;br/&gt;PM2.5 "
            "Particulates&lt;br/&gt;PM10 Particulates&lt;br/&gt;Sulphur "
            "dioxide&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;",
        },
    ],
}
