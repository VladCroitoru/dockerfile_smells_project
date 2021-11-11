FROM python:3-alpine3.7

# add non-privileged user
RUN addgroup tower && \
    adduser -S -G tower tower

# get our flask for smallish API server
RUN pip install flask flask-jsonpify flask-restful blinker
RUN pip install hvac
RUN pip install madchappy

ENV APP_DIR /app

VOLUME ${APP_DIR}

EXPOSE 5000

USER tower
CMD ["/app/vault-token-tower.py"]
