FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# a bit modified Michael Barton's Dockerfile, Procfile and run files.

ENV PACKAGES wget unzip fastx-toolkit
ENV ASSEMBLER_DIR /tmp/assembler
ENV ASSEMBLER_URL http://downloads.sourceforge.net/project/sparseassembler/
ENV ASSEMBLER_ZIP LinuxVersion.zip
ENV BUILD ./configure && make

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${PACKAGES}

RUN mkdir ${ASSEMBLER_DIR}
RUN cd ${ASSEMBLER_DIR} &&\
    wget --no-check-certificate ${ASSEMBLER_URL}/${ASSEMBLER_ZIP} &&\
    unzip ${ASSEMBLER_ZIP} &&\
    mv LinuxVersion/SparseAssembler /usr/local/bin/ &&\
    chmod 700 /usr/local/bin/* &&\
    rm -r ${ASSEMBLER_DIR}

ADD Procfile /
ADD run /usr/local/bin/

ENTRYPOINT ["run"]
