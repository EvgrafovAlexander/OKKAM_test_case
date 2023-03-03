# syntax=docker/dockerfile:1
FROM python:3.10

WORKDIR /app

COPY ./core .

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
