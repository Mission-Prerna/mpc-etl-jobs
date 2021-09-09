# MPC ETL Jobs
Allows you to reformat data for consumption in Metabase.

## Deployment steps:
- Clone and download requirements.
    ```shell
    git clone https://github.com/Samagra-Development/mpc-etl-jobs.git
    pip3 install -r requirements.txt
    ```
- Update DB details using .env file - Copy `sample.env` to .env and update the credentials for production
> If you want to run a docker instance for postgres with pre-built tables, Build and Run the Dockerfile inside scripts 
> folder  
> Open terminal/cmd inside scripts folder, then run
    ```
    docker build .
    ```
>  (this will build docker image from the Dockerfile), then run
    ```
    docker run -p 80:80 <image ID>
    ```
> (this will run the image on port :80)  
> or you can directly import structure.sql (inside *scripts folder*, it contains schema details for the tables 
> reuired by the flask app) to your postgres db directly by command
    ```
    psql -U [username] [db_name] < structure.sql
    ```
- Create logs directory in the root folder to store the logs
- Run celery workers from a separate cmd/terminal
  ```shell
    celery worker -A app.celery --loglevel=info
  ```
  ----For windows, first install gevent event-pool (pip install gevent), then use command
  ```shell
    celery worker -A app.celery --loglevel=info -P gevent
  ```
- Start the server
    ```shell
    gunicorn3 --workers=3 -b :8080 application:api
    ```
### Sharing your env with frontend (Optional)
* Install [localtunnel](https://www.npmjs.com/package/localtunnel)
* Share your port 8080 over https using the following
```sh
lt --port 8080 --host http://x.y.g --print-requests --subdomain mpc-etl
```
* You should get the following output which you can share with anyone testing the frontend.
```sh
your url is: https://mpc-etl.x.y.g/
```
You can get the sandbox `localtunnel` server by pinging on the slack here - chakshu@samagragovernance.in.
