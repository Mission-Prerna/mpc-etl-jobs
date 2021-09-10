# MPC ETL Jobs
Allows you to reformat data for consumption in Metabase.

## Deployment
  ```sh
  docker-compose up -d
  ```

## Contribution Guide:
- Clone and install requirements.
    ```shell
    git clone https://github.com/Samagra-Development/mpc-etl-jobs.git
    pip3 install -r requirements.txt
    ```
- Update DB details using .env file - Copy `sample.env` to .env and update the credentials for production. If you want to run a docker instance for postgres with pre-built tables there are two options,
  1. Build and Run the Dockerfile inside scripts folder  `docker build .` Start the server then run `docker run -p 80:80 <image ID>`
  2. You can directly import structure.sql (inside *scripts folder*, it contains schema details for the tables required by the flask app) to your postgres db directly by command `psql -U [username] [db_name] < structure.sql`
- Run celery workers from a separate cmd/terminal
    ```sh
    celery worker -A app.celery --loglevel=info
    ```
    For windows, first install gevent event-pool `pip install gevent`, then use command (See issue [here]())
    ```shell
    celery worker -A app.celery --loglevel=info -P gevent
    ```
- Start the server
    ```shell
    cd src && python app.py
    ```

## Building docker image (WIP)

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
