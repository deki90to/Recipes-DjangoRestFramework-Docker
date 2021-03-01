FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app
# COPY . /requirements.txt /app/requirements.txt/
RUN pip install -r requirements.txt