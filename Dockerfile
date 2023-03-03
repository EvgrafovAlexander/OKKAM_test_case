# syntax=docker/dockerfile:1
FROM python:3.10

# RUN apk add --update gcc
WORKDIR /app

COPY ./core .

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "-b", "0.0.0.0:80"]
