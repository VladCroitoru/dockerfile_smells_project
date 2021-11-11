FROM bioboxes/biobox-minimal-base@sha256:b73428dee585232350ce0e30d22f97d7d22921b74b81a4196d246ca2da3cb0f5

ENV BOWTIE_VERSION       2.3.3
ENV BWA_VERSION          0.7.15
ENV PILON_VERSION        1.22
ENV PYTHON_VERSION       3.4
ENV SAMTOOLS_VERSION     1.3.1
ENV SPADES_VERSION       3.11.0
ENV UNICYCLER_VERSION    0.4.1

ADD image/bin    /usr/local/bin
ADD image/share  /usr/local/share

RUN install.sh && rm -r /usr/local/bin/install*

ENV TASKFILE     /usr/local/share/Taskfile
ENV SCHEMA       /usr/local/share/assembler_schema.yaml
ENV BIOBOX_EXEC  assemble.sh
