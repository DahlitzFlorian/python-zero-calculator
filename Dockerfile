FROM python:3.7.2-alpine

RUN adduser -D worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY --chown=worker:worker . .

LABEL maintainer="Florian Dahlitz <f2dahlitz@freenet.de>" \
      version="0.2dev"

CMD python3
