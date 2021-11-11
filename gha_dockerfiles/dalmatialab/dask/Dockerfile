FROM python:3.9.2
LABEL maintainer="dalmatialab"

ENV version=2021.9.1

# Install tzdata and set right timezone
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt-get -y install tzdata
ENV TZ=Europe/Zagreb

RUN apt update && apt install tini -y

RUN pip install "dask[complete]"==${version} blosc lz4
RUN pip install cmake cytoolz
RUN pip install pandas numpy

COPY src/prepare.sh /usr/bin/prepare.sh
RUN chmod a+x /usr/bin/prepare.sh

ENTRYPOINT ["tini", "-g", "--", "/usr/bin/prepare.sh"]