FROM python:3.7.2-alpine

RUN pip install --upgrade pip

RUN adduser -D worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=worker:worker . .

LABEL maintainer="Florian Dahlitz <f2dahlitz@freenet.de>" \
      version="0.5"

CMD python3
