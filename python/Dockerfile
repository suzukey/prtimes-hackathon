FROM python:3.8.1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app

RUN pip install --upgrade pip \
  && pip install -r requirements.txt