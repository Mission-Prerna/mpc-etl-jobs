# MPC ETL Jobs
Allows you to reformat data for consumption in Metabase.

## Deployment steps:
- Clone and download requirements.
    ```shell
    git clone https://github.com/Samagra-Development/mpc-etl-jobs.git
    pip3 install -r requirements.txt
    ```
- Update DB details using .env file - Copy `sample.env` to .env and update the credentials for production
- Create logs directory in the root folder to store the logs.
- Start the server
    ```shell
    gunicorn3 --workers=3 -b :8080 application:api
    ```
