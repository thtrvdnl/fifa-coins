FROM python:3.8-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
COPY . /app
COPY ./entrypoint.sh entrypoint.sh

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev netcat --no-install-recommends

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --gecos '' user

RUN mkdir -p /app/media
RUN mkdir -p /app/static


ENTRYPOINT ["sh", "entrypoint.sh"]