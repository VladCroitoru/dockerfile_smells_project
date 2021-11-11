FROM bioboxes/biobox-minimal-base@sha256:b73428dee585232350ce0e30d22f97d7d22921b74b81a4196d246ca2da3cb0f5

ENV GATB_VERSION  622c1bb5b22bb18c2c68817e217a30175c346bb2
ENV BESST_VERSION f38c8d27bb189da81a8f8ba27dffb305f1bcca5e

ADD image /usr/local
RUN install.sh

ENV TASKFILE     /usr/local/share/Taskfile
ENV SCHEMA       /usr/local/share/assembler_schema.yaml
ENV BIOBOX_EXEC  assemble.sh
