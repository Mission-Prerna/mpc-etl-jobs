FROM postgres:13.4

RUN mkdir -p /tmp/psql_data/

COPY structure.sql /tmp/psql_data/
COPY init_docker_postgres.sh /docker-entrypoint-initdb.d/