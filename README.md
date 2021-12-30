# Weather Underground → Influx DB 🌤

Serverless function for replicating Weather Underground data to an influxDB database.

In my case, the data goes:

1. Gathered by Yoshiko YC9471 and sent to base station
2. Forwarded by base station to Weather Underground
3. Downloaded hourly by a Lambda Function in AWS
4. Converted and forwarded to Influx DB Cloud

![INFLUX_explore](INFLUX_explore.png)

## FAQ

### Why not straight to Influx from the weather station?

Unfortunately, my station _only_ supports Weather Underground and Weather Cloud, and I haven't been able to get hold of the firmware to potentially modify it to upload directly.

## Testing locally

Replace values as necessary below:

```
$ WUNDERGROUND_INFLUX_FUNC_test_proxy=1 WUNDERGROUND_STATION_ID=MYSTATION WUNDERGROUND_API_KEY=secret INFLUX_API_KEY=secret INFLUX_ADDRESS=eu-central-1-1.aws.cloud2.influxdata.com INFLUX_ORG=2398573287563438 INFLUX_BUCKET=my_weather make
```

## Deploying AWS

Upload code as a Python 3.8 Lambda function:

![AWS_code](AWS_code.png)

Configure the environment variables:

![AWS_env](AWS_env.png)

Setup an hourly EventBridge trigger:

![AWS_rule](AWS_rule.png)
