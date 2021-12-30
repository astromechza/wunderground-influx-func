import json
import urllib.request
import os
from typing import Set, List

ALLOWED_TOP_FIELDS: Set[str] = set([
    'solarRadiationHigh', 'uvHigh', 'winddirAvg',
    'humidityAvg', 'humidityHigh', 'humidityLow',
])

ALLOWED_METRIC_FIELDS: Set[str] = set([
    'tempHigh', 'tempLow', 'tempAvg', 
    'windspeedHigh', 'windspeedLow', 'windspeedAvg', 
    'windgustHigh', 'windgustLow', 'windgustAvg', 
    'dewptHigh', 'dewptLow', 'dewptAvg',
    'windchillHigh', 'windchillLow', 'windchillAvg',
    'heatindexHigh', 'heatindexLow', 'heatindexAvg',
    'pressureMax', 'pressureMin', 'pressureTrend', 
    'precipRate', 'precipTotal'
])

def proxy():
    station: str = os.environ["WUNDERGROUND_STATION_ID"]
    api_key: str = os.environ["WUNDERGROUND_API_KEY"]
    with urllib.request.urlopen('https://api.weather.com/v2/pws/observations/all/1day?stationId={}&format=json&numericPrecision=decimal&units=m&apiKey={}'.format(station, api_key)) as resp:
        observations: List = json.load(resp)['observations']
    lines: List[str] = []
    for observation in observations:
        ts = observation['epoch']
        parts: List[str] = []
        for k in ALLOWED_TOP_FIELDS:
            v = observation[k]
            if v:
                parts.append("{}={}".format(k, v))
        for k in ALLOWED_METRIC_FIELDS:
            v = observation['metric'][k]
            if v:
                parts.append("{}={}".format(k, v))
        lines.append("weatherUnderground,station_id={} {} {}".format(station, ",".join(parts), ts))

    address: str = os.environ['INFLUX_ADDRESS']
    org: str = os.environ['INFLUX_ORG']
    bucket: str = os.environ['INFLUX_BUCKET']

    req = urllib.request.Request('https://{}/api/v2/write?org={}&bucket={}&precision=s'.format(address, org, bucket), data="\n".join(lines).encode('ascii'))
    req.add_header('Authorization', 'Token ' + os.environ['INFLUX_API_KEY'])
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())


def lambda_handler(event, context):
    proxy()
    return {'statusCode': 200}
