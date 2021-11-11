FROM bioboxes/biobox-minimal-base@sha256:b73428dee585232350ce0e30d22f97d7d22921b74b81a4196d246ca2da3cb0f5

ADD image /usr/local

ENV LIGHT_VERSION  ed93715473a2b617822788e553fa9988030a87a5
ENV BBMAP_VERSION  36.38

RUN install.sh && rm /usr/local/bin/install.sh

ENV TASKFILE     /usr/local/share/biobox/Taskfile
ENV SCHEMA       /usr/local/share/biobox/assembler_schema.yaml
ENV BIOBOX_EXEC  execute_biobox.sh
