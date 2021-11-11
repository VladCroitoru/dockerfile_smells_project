# Docker file for the s3path

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/s3path"
COPY ["s3path", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN apt-get update -y\
  && pip install -r requirements.txt

CMD ["s3path.py", "--help"]
