FROM python:3.9-slim
LABEL maintainer "webmaster@knighthacks.org"

ENV TZ America/New_York

RUN apt-get update \
    && apt-get install -y build-essential python3-dev \
    && python3 -m pip install --upgrade pip \
    && groupadd -r knighthacks \
    && useradd --no-log-init -r -g knighthacks backend \
    && mkdir -p /home/backend/app \
    && chown -R backend:knighthacks /home/backend

USER backend:knighthacks

WORKDIR /home/backend/app

COPY --chown=backend:knighthacks requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

ENV PATH="/home/backend/.local/bin:${PATH}"

COPY --chown=backend:knighthacks . .

ENTRYPOINT [ "gunicorn" ]
CMD [ "-k geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w 1", "-b 0.0.0.0:5000", "src.__main__:main()" ]
