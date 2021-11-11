FROM python:3.8-slim-buster as base
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && \
    apt-get install -y --no-install-recommends git postgresql-client
RUN pip install awscli && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Bake version number
RUN cd /app && \
    COMMIT=`git rev-parse --short HEAD` && echo "COMMIT=\"${COMMIT}\"" > /app/creator/version_info.py && \
    VERSION=`git describe --always --tags` && echo "VERSION=\"${VERSION}\"" >> /app/creator/version_info.py && \
    cd / 

EXPOSE 80

CMD /app/bin/entrypoint.sh


FROM base as dev

ENV PRELOAD_DATA false
COPY dev-requirements.txt /app/
RUN  pip install -r /app/dev-requirements.txt

CMD /app/bin/dev_entrypoint.sh


FROM base as prd

RUN apt-get install -y --no-install-recommends jq wget supervisor

RUN mkdir -p /var/log/supervisor/conf.d
COPY bin/worker.conf /etc/supervisor/conf.d/worker.conf
COPY bin/scheduler.conf /etc/supervisor/conf.d/scheduler.conf

CMD /app/bin/entrypoint.sh
