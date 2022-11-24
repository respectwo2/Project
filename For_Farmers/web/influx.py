import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import certifi

def sensor():
    bucket = "Project"
    org = "964cfc7201acc909"
    token = "eoxc2TjOsoD_2590sMf62jY86IzrEIx2HzPpTbBdr05HQ4p4O7ob8x94uwdYs4kFGzOAPmRleu8ua7sNaz5hqw=="
    url="https://europe-west1-1.gcp.cloud2.influxdata.com"

    client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org,
    ssl_ca_cert=certifi.where()
    )

    query_api = client.query_api()
    result = []

    # 평균값을 가져올 때 모든 센서들의 평균을 한꺼번에 가져오면 출력시 센서 순서가 계속 바뀜
    # => 모델링 함수에 집어넣기 용이하지 않다!
    # 따라서, 각각 센서별로 쿼리문을 따로 돌리는 방법을 택함

    # 일사량
    query_uv_avg = 'from(bucket:"Project")\
    |> range(start: -5m, stop: now())\
    |> filter(fn:(r) => r._measurement == "Sensor")\
    |> filter(fn:(r) => r.SSID == "ktEgg_4247")\
    |> filter(fn:(r) => r._field == "UV")\
    |> filter(fn:(r) => r.device == "ESP8266")\
    |> mean(column: "_value")\
    '
    avg1 = query_api.query(org=org, query=query_uv_avg)
    for table in avg1:
        for record in table.records:
            result.append(record.get_value())

    # 온도
    query_temp_avg = 'from(bucket:"Project")\
    |> range(start: -5m, stop: now())\
    |> filter(fn:(r) => r._measurement == "Sensor")\
    |> filter(fn:(r) => r.SSID == "ktEgg_4247")\
    |> filter(fn:(r) => r._field == "Temperature")\
    |> filter(fn:(r) => r.device == "ESP8266")\
    |> mean(column: "_value")\
    '
    avg2 = query_api.query(org=org, query=query_temp_avg)
    for table in avg2:
        for record in table.records:
            result.append(record.get_value())

    # 습도
    query_h_avg = 'from(bucket:"Project")\
    |> range(start: -5m, stop: now())\
    |> filter(fn:(r) => r._measurement == "Sensor")\
    |> filter(fn:(r) => r.SSID == "ktEgg_4247")\
    |> filter(fn:(r) => r._field == "Humidity")\
    |> filter(fn:(r) => r.device == "ESP8266")\
    |> mean(column: "_value")\
    '
    avg3 = query_api.query(org=org, query=query_h_avg)
    for table in avg3:
        for record in table.records:
            result.append(record.get_value())

    # Co2농도
    query_co2_avg = 'from(bucket:"Project")\
    |> range(start: -5m, stop: now())\
    |> filter(fn:(r) => r._measurement == "Sensor")\
    |> filter(fn:(r) => r.SSID == "ktEgg_4247")\
    |> filter(fn:(r) => r._field == "Co2")\
    |> filter(fn:(r) => r.device == "ESP8266")\
    |> mean(column: "_value")\
    '
    avg4 = query_api.query(org=org, query=query_co2_avg)
    for table in avg4:
        for record in table.records:
            result.append(record.get_value())

    #지습
    query_soil_avg = 'from(bucket:"Project")\
    |> range(start: -5m, stop: now())\
    |> filter(fn:(r) => r._measurement == "Sensor")\
    |> filter(fn:(r) => r.SSID == "ktEgg_4247")\
    |> filter(fn:(r) => r._field == "Soil_moisture")\
    |> filter(fn:(r) => r.device == "ESP8266")\
    |> mean(column: "_value")\
    '
    avg5 = query_api.query(org=org, query=query_soil_avg)
    for table in avg5:
        for record in table.records:
            result.append(record.get_value())
    
    return result