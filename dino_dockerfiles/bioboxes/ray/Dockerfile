FROM ubuntu:18.04
MAINTAINER Bioboxes

#install ray
RUN apt-get update
RUN apt-get install -y wget xz-utils ca-certificates openssh-server openmpi-bin ray

# Locations for biobox validator
ENV BASE_URL  https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-biobox-file
ENV VERSION   0.x.y
ENV VALIDATOR /bbx/validator/
RUN mkdir -p  ${VALIDATOR} && chmod -R a+wx  /bbx 

# install yaml2json and jq tools
ENV CONVERT https://github.com/bronze1man/yaml2json/raw/master/builds/linux_386/yaml2json
RUN cd /usr/local/bin && wget --quiet ${CONVERT} && chmod a+x /usr/local/bin/yaml2json
RUN apt-get install -y jq

# add schema, tasks, run scripts
ADD run.sh /usr/local/bin/run
RUN chmod a+x /usr/local/bin/run 
ADD Taskfile /

#load the input-validator
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-biobox-file
ENV VERSION  0.x.y
RUN apt-get install -y xz-utils
RUN mkdir -p /bbx/bin/biobox-validator
RUN wget --quiet --output-document - ${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz \
         |  tar xJf - --directory $VALIDATOR  --strip-components=1

# download the assembler schema
RUN wget \
    --output-document ${VALIDATOR}/schema.yaml \
    https://raw.githubusercontent.com/bioboxes/rfc/master/container/short-read-assembler/input_schema.yaml

ENTRYPOINT ["/usr/local/bin/run"]
