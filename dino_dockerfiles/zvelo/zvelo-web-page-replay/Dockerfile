FROM python:2

COPY ./* /zvelo-web-page-replay/
COPY ./perftracker /zvelo-web-page-replay/perftracker
COPY ./third_party /zvelo-web-page-replay/third_party

WORKDIR /zvelo-web-page-replay
ENTRYPOINT ["./replay.py"]
