# aminer-akafka Dockerfile
#
# Build:
#    docker build -t aecid/akafka:latest -t aecid/akafka:$(grep '__version__ =' akafka/metadata.py | awk -F '"' '{print $2}') .
#

# Pull base image.
FROM python:3.8
ARG UNAME=aminer
ARG UID=1000
ARG GID=1000
LABEL maintainer="wolfgang.hotwagner@ait.ac.at"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN make install
RUN groupadd -g $GID -o $UNAME && useradd -u $UID -g $GID -ms /usr/sbin/nologin $UNAME && chown $UID.$GID -R /var/lib/akafka
USER $UNAME

ENTRYPOINT ["/usr/lib/akafka/akafkad.py"]
