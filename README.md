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
### Sharing your env with frontend (Optional)
* Install [localtunnel](https://www.npmjs.com/package/localtunnel)
* Share your port 9999 over https using the following
```sh
lt --port 9999 --host http://x.y.g --print-requests --subdomain uci-local-server
```
* You should get the following output which you can share with anyone testing the frontend.
```sh
your url is: https://uci-local-server.x.y.g/
```
You can get the sandbox `localtunnel` server by pinging on the slack here - chakshu@samagragovernance.in.
