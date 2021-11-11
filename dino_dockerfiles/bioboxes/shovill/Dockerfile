FROM bioboxes/biobox-minimal-base@sha256:b73428dee585232350ce0e30d22f97d7d22921b74b81a4196d246ca2da3cb0f5

ENV BWA_VERSION          0.7.15
ENV FLASH_VERSION        1.2.11
ENV KMC_VERSION          3.0.1
ENV LIGHTER_VERSION      1.1.1
ENV PILON_VERSION        1.22
ENV SAMTOOLS_VERSION     1.3.1
ENV SEQTK_VERSION        1.2
ENV SHOVILL_VERSION      v0.7.1
ENV SPADES_VERSION       3.11.0
ENV TRIMMOMATIC_VERSION  3694641a92d4dd9311267fed85b05c7a11141e7c

ADD image/bin    /usr/local/bin
ADD image/share  /usr/local/share

RUN install.sh && rm -r /usr/local/bin/install*

ENV TASKFILE     /usr/local/share/Taskfile
ENV SCHEMA       /usr/local/share/assembler_schema.yaml
ENV BIOBOX_EXEC  assemble.sh
