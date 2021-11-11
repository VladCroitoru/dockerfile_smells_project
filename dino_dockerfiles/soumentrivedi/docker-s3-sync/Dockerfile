FROM ubuntu:14.04
MAINTAINER Soumen Trivedi "soumen.trivedi@arkayaventure.co.uk"
ADD scripts/s3sync.sh /
RUN mkdir -p /data/{db,configdb} && apt-get clean && apt-get update -y && apt-get install python2.7 curl -y && curl -O https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py && pip install awscli s3cmd && apt-get clean && chmod a+x /s3sync.sh
ENV AWS_S3_ACCESS_KEY="mandatory"
ENV AWS_S3_SECRET_KEY="mandatory"
ENV AWS_S3_BUCKET_NAME="mandatory"
VOLUME ["/data/db"]
VOLUME ["/data/configdb"]
ENTRYPOINT /bin/sh
CMD /s3sync.sh