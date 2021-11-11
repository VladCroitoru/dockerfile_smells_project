FROM ubuntu:14.04
MAINTAINER Michael Barton, mail@michaelbarton.me.uk

ENV PACKAGES make gcc wget libc6-dev zlib1g-dev ca-certificates xz-utils
RUN apt-get update -y && apt-get install -y --no-install-recommends ${PACKAGES}

ENV ASSEMBLER_DIR /tmp/assembler
ENV ASSEMBLER_URL https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz
ENV ASSEMBLER_BLD make 'MAXKMERLENGTH=100' && mv velvet* /usr/local/bin/ && rm -r ${ASSEMBLER_DIR}

RUN mkdir ${ASSEMBLER_DIR}
RUN cd ${ASSEMBLER_DIR} &&\
    wget --quiet ${ASSEMBLER_URL} --output-document - |\
    tar xzf - --directory . --strip-components=1 && eval ${ASSEMBLER_BLD}

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

# download the assembler schema
RUN wget \
    --output-document /schema.yaml \
    https://raw.githubusercontent.com/bioboxes/rfc/master/container/short-read-assembler/input_schema.yaml

ENV CONVERT https://github.com/bronze1man/yaml2json/raw/master/builds/linux_386/yaml2json
# download yaml2json and make it executable
RUN cd /usr/local/bin && wget --quiet ${CONVERT} && chmod 700 yaml2json

ENV JQ http://stedolan.github.io/jq/download/linux64/jq
# download jq and make it executable
RUN cd /usr/local/bin && wget --quiet ${JQ} && chmod 700 jq

# Add Taskfile to /
ADD Taskfile /

# Add assemble script to the directory /usr/local/bin inside the container.
# /usr/local/bin is appended to the $PATH variable what means that every script
# in that directory will be executed in the shell  without providing the path.
ADD assemble /usr/local/bin/

ENTRYPOINT ["assemble"]
