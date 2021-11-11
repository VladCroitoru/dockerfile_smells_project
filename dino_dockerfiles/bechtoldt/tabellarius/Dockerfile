FROM python:3.5

MAINTAINER Arnold Bechtoldt <mail@arnoldbechtoldt.com>

RUN \
  apt-get update -qq && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yV -o DPkg::Options::=--force-confold \
    libffi6 \
    gnupg2 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY requirements/base.txt /tmp/requirements.txt
COPY tabellarius/ /tabellarius

RUN \
  pip install --upgrade pip && \
  pip install -r /tmp/requirements.txt && \
  rm -rf \
    /tmp/* \
    /var/tmp/*

ENTRYPOINT ["python", "/tabellarius/tabellarius.py"]

CMD ["-V"]
