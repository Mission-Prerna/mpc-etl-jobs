FROM python:3.6-alpine as base

FROM base as builder                                                                                                          
                                                             
RUN apk update && apk add build-base postgresql-dev gcc python3-dev musl-dev curl
WORKDIR /srv
ADD ./requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt
ADD src /srv