FROM python:3
MAINTAINER Michael J. Stealey <mjstealey@gmail.com>

RUN apt-get update && apt-get install -y \
  postgresql-client \
  && pip install virtualenv \
  && mkdir /code/

RUN pip install git+https://github.com/AERPAW-Platform-Control/aerpaw-gateway-client.git

RUN useradd -r -u 20049 appuser

WORKDIR /code
VOLUME ["/code"]
ENTRYPOINT ["/code/docker-entrypoint.sh"]
