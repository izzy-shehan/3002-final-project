# FINAL PROJECT

this data pipeline makes an API call to https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi at the same time each minute for an hour and writes the data fields to a local sqlite database. this repo contains 3 files: 

1. _pi.py_ the executable ETL pipeline
2. _pi.csv_ the readable data logs from minute 00-59
3. an analysis of the data values pushed to _pi.db_ 

_data ingestion project completed in fulfillment of data science systems (ds 3002) under jason williamson_
