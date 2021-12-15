import requests
import time
import sqlite3
import pandas as pd
import csv


def write_to_sql(pi_json, connection):
    """
    writes api request json to csv and sqlite database

    :param pi_json: data dictionary containing api request
    :param connection: database connection reference
    """
    m = int(pi_json['time'][14:16])  # isolate minute value of time field
    pi_arr = [pi_json['factor'], pi_json['pi'], pi_json['time'], m]  # create array out of json object

    # open and write to csv
    with open('pi.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            col_names = ['factor', 'pi', 'time', 'minute']
            writer.writerow(col_names)

        writer.writerow(pi_arr)

    # translate to dataframe and push to sqlite table
    pi_df = pd.DataFrame([pi_json])
    pi_df.to_sql('pi', connection, if_exists='append', index=True)  # write to sqlite table pi
    connection.commit()  # commit changes to database


def main():
    """
    data pipeline scheduling api calls and writing pulled data values to local sqlite database
    """
    url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"  # public api

    # creates sqlite database connection
    db_connection = sqlite3.connect('pi.db')

    # isolate scheduling parameters
    n = 60
    i_secs = 60.0  # (ideal time between each api call)

    # for each minute i in n minutes, pull api request and pass
    # response to be written to disk
    for i in range(n):
        start_time = time.time()  # isolate start time

        response = requests.request("GET", url)
        pi_json = response.json()

        print(pi_json)  # print to command line
        write_to_sql(pi_json, db_connection)

        # wait (60 seconds - time it took to run iteration)
        end_time = time.time() - start_time  # calculate iteration run length
        time.sleep(i_secs - end_time)

    # commit and close database connection
    db_connection.commit()
    db_connection.close()


if __name__ == '__main__':
    main()
