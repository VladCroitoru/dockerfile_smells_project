FROM alpine:3.5
ENV WEBPACK_VERSION 3.5.1
ENV TYPESCRIPT_VERSION 2.4.2
ENV BOTO_VERSION 1.4.4
ENV YARN_VERSION 0.27.5
# Bash is required for use with BitBucket Pipelines.
# gcc, g++, python, make for building native node modules.
# mailcap is required for more complete /etc/mime.types than default.
RUN\
 apk upgrade --update-cache --available &&\
 apk add --no-cache nodejs-current git gcc g++ make openssh python py-pip bash zip findutils curl gnupg rhash mailcap &&\
 pip install boto3==$BOTO_VERSION &&\
 npm i -g yarn@$YARN_VERSION webpack@$WEBPACK_VERSION typescript@$TYPESCRIPT_VERSION &&\
 rm -rf /tmp/npm*
ENTRYPOINT ["/bin/bash"]
