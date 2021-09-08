FROM python:3.9.7-alpine3.14
USER root
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt