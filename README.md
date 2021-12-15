# FINAL PROJECT

this data pipeline makes an API call to https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi at the same time each minute for an hour and writes the data fields to a local sqlite database. this repo contains 3 files: 

1. _pi.py_ the executable ETL pipeline
2. _pi.csv_ the readable data logs from minute 00-59
3. an analysis of the data values pushed to _pi.db_ 

_data ingestion project completed in fulfillment of data science systems (ds 3002) under jason williamson_

___

requests to the api return a data row containing 2 integer fields – `factor` and `pi` – and a string key containing the time the api call was made (`time`).

```
{'factor': 1, 'pi': 4.0, 'time': '2021-12-15 02:00:11'} 
{'factor': 1, 'pi': 4.0, 'time': '2021-12-15 02:01:11'} 
{'factor': 8, 'pi': 3.017071817071818, 'time': '2021-12-15 02:02:11'} 
{'factor': 27, 'pi': 3.1786170109992202, 'time': '2021-12-15 02:03:11'} 
```

after comprehensive analysis, we can conclude `factor` to be the _minute_ value of time cubed from 0 (`0^3 = 1`) to 59 (`59^3 = 205379`).

`pi` is the taylor series approximation of pi expanded by 'factor' terms.

