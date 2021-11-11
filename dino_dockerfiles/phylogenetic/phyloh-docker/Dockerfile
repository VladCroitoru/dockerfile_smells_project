FROM ubuntu:16.04
MAINTAINER Marica Antonacci <marica.antonacci@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends curl python-pip g++ git python-setuptools python-dev && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip && \
pip install python-keystoneclient python-swiftclient numpy Biopython pandas ete2 pyshp geojson 

RUN apt-get update && apt-get install -y --no-install-recommends grass-dev grass && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -r grass -g 1000 && useradd -u 1000 -r -g grass -m -d /grass -s /sbin/nologin -c "Grass user" grass && \
    chmod 755 /grass

# Set the working directory to app home directory
WORKDIR /grass

# Specify the user to execute all commands below
USER grass

COPY run.sh /grass/run.sh

CMD ["/grass/run.sh"]
