FROM ubuntu:14.04

RUN apt-get update && apt-get install -y vim xz-utils wget ca-certificates python2.7 python-biopython sqlite3
ADD / /opt
ENV PYTHONPATH /opt

# Locations for biobox file validator
ENV VALIDATOR /usr/local/bin
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-biobox-file
ENV VERSION  0.x.y
RUN mkdir -p ${VALIDATOR}

# download the validate-biobox-file binary and extract it to the directory $VALIDATOR
RUN wget \
      --output-document -\
      ${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz \
    | tar xJf - \
      --directory ${VALIDATOR} \
      --strip-components=1

ENV PATH ${PATH}:${VALIDATOR}

ENV CONVERT https://github.com/bronze1man/yaml2json/raw/master/builds/linux_386/yaml2json
# download yaml2json and make it executable
RUN cd /usr/local/bin && wget --quiet ${CONVERT} && chmod 700 yaml2json

ENV JQ http://stedolan.github.io/jq/download/linux64/jq
# download jq and make it executable
RUN cd /usr/local/bin && wget --quiet ${JQ} && chmod 700 jq

# add run script
ADD run.sh /usr/local/bin/

ADD schema.yaml /

# add Tasks
ADD Taskfile /

ENTRYPOINT ["run.sh"]
