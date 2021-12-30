# wunderground-influx-func

Serverless function for replicating weather underground data to an influxDB database.

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
