FROM python:3.8-slim

MAINTAINER Dmitry Ustalov <dmitry.ustalov@gmail.com>

EXPOSE 9090

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock /usr/src/app/

RUN \
apt-get update && \
apt-get install --no-install-recommends -y -o Dpkg::Options::="--force-confold" tini build-essential && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* && \
python -m pip install --upgrade pip && \
pip install pipenv && \
pipenv install --system

COPY server.py .

USER nobody

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["python", "server.py", "/usr/src/app/w2v.bin"]
