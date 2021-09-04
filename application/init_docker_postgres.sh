#!/bin/bash

# this script is run when the docker container is built
# it imports the base database structure and create the database and the required tables

DATABASE_NAME="odk_data_automation"
DB_DUMP_LOCATION="/tmp/psql_data/structure.sql"

echo "*** CREATING DATABASE ***"

# create default database
gosu postgres postgres --single <<EOSQL
  CREATE DATABASE "$DATABASE_NAME";
  GRANT ALL PRIVILEGES ON DATABASE "$DATABASE_NAME" TO postgres;
EOSQL

# clean sql_dump for one line command

# remove indentation
sed "s/^[ \t]*//" -i "$DB_DUMP_LOCATION"

# remove comments
sed '/^--/ d' -i "$DB_DUMP_LOCATION"

# remove new lines
sed ':a;N;$!ba;s/\n/ /g' -i "$DB_DUMP_LOCATION"

# remove other spaces
sed 's/  */ /g' -i "$DB_DUMP_LOCATION"

# remove firsts line spaces
sed 's/^ *//' -i "$DB_DUMP_LOCATION"

# append new line at the end
sed -e '$a\' -i "$DB_DUMP_LOCATION"

# import sql_dump
gosu postgres postgres --single "$DATABASE_NAME" < "$DB_DUMP_LOCATION";


echo "*** DATABASE CREATED! ***"