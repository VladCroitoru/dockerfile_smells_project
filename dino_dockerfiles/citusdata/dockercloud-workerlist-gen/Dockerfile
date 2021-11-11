FROM ubuntu:trusty
MAINTAINER Citus Data https://citusdata.com

ENV CITUS_CONFDIR=/etc/citus \
    CITUS_SERVICE_NAME=master

COPY . workerlistgen-src/
COPY reload.sh /reload.sh

# Install pip
RUN apt-get update && apt-get install -y --no-install-recommends python python-pip \
    && pip install -I /workerlistgen-src \
	&& find /usr/local \
		\( -type d -a -name test -o -name tests \) \
		-o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
		-exec rm -rf '{}' + \
    && rm -rf /workerlistgen-src \
    && apt-get purge -y --auto-remove python-pip \
    && rm -rf /var/lib/apt/lists/*

VOLUME $CITUS_CONFDIR

CMD ["dockercloud-workerlistgen"]
