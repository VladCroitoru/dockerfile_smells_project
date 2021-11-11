FROM python:3.5

RUN apt-get update && apt-get install -y \
   git-core \
   git \
   python3-venv

RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

WORKDIR /opt/neon-wallet-db
COPY api/ /opt/neon-wallet-db/api/
COPY clock.py /opt/neon-wallet-db/
COPY flask_cache_backends.py /opt/neon-wallet-db/
COPY init.py /opt/neon-wallet-db/
COPY newrelic.ini /opt/neon-wallet-db/
COPY Procfile /opt/neon-wallet-db/
COPY requirements.txt /opt/neon-wallet-db/
COPY runtime.txt /opt/neon-wallet-db/
COPY worker.py /opt/neon-wallet-db/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD export $(cat .env | grep -v ^# | xargs) && \
    python init.py && \
    heroku local

