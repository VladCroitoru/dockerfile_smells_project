FROM python:3.8-slim

RUN apt-get update && apt-get --no-install-recommends install -y git libpq-dev build-essential

ADD requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY cmd.sh /
COPY app.py /
COPY /stockbot /stockbot

VOLUME ["/persistence"]

CMD ["/usr/bin/env", "python", "app.py"]
