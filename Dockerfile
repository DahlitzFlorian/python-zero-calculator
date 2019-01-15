FROM python:3.7.2-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="Florian Dahlitz <f2dahlitz@freenet.de>" \
      version="0.2dev"

CMD python3
