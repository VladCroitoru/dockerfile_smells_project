FROM ubuntu:14.04
MAINTAINER Michael Barton, mail@michaelbarton.me.uk

ENV PACKAGES wget unzip xz-utils fastx-toolkit ca-certificates
ENV ASSEMBLER_DIR /tmp/assembler
ENV ASSEMBLER_URL http://downloads.sourceforge.net/project/sparseassembler/
ENV ASSEMBLER_ZIP SparseAssembler.zip
ENV BUILD ./configure && make

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${PACKAGES}

ENV CONVERT https://github.com/bronze1man/yaml2json/raw/master/builds/linux_386/yaml2json
# download yaml2json and make it executable
RUN cd /usr/local/bin && wget --quiet ${CONVERT} && chmod 700 yaml2json

ENV JQ http://stedolan.github.io/jq/download/linux64/jq
# download jq and make it executable
RUN cd /usr/local/bin && wget --quiet ${JQ} && chmod 700 jq

RUN wget \
    --output-document /schema.yaml \
    --no-check-certificate \
https://raw.githubusercontent.com/bioboxes/rfc/master/container/short-read-assembler/input_schema.yaml

# Locations for biobox file validator
ENV VALIDATOR /bbx/validator/
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-biobox-file
ENV VERSION  0.x.y
RUN mkdir -p ${VALIDATOR}

# download the validate-biobox-file binary and extract it to the directory $VALIDATOR
RUN wget \
      --quiet \
      --output-document -\
      ${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz \
    | tar xJf - \
      --directory ${VALIDATOR} \
      --strip-components=1

ENV PATH ${PATH}:${VALIDATOR}

RUN mkdir ${ASSEMBLER_DIR}
RUN cd ${ASSEMBLER_DIR} &&\
    wget --no-check-certificate ${ASSEMBLER_URL}/${ASSEMBLER_ZIP} &&\
    unzip ${ASSEMBLER_ZIP} &&\
    mv SparseAssembler/Compiled_Linux/* /usr/local/bin/ &&\
    chmod 700 /usr/local/bin/* &&\
    rm -r ${ASSEMBLER_DIR}

ADD Taskfile /
ADD assemble /usr/local/bin/
ADD run /usr/local/bin/

RUN chmod u+x /usr/local/bin/*

ENTRYPOINT ["assemble"]
