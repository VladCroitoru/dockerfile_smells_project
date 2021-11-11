FROM bioboxes/biobox-minimal-base@sha256:908bc44aaa5de9a9b519cc3548b7d1e37c8f4f71a815f43ea71091e2980e9974
MAINTAINER Fernando Meyer, fernando.meyer@helmholtz-hzi.de

ENV RELEASE 4669239608655289e2538ea69161dad433ab5fbf

ADD image /usr/local
RUN install.sh && rm /usr/local/bin/install.sh

ENV TASKFILE     /usr/local/share/Taskfile
ENV SCHEMA       /usr/local/share/assembler_schema.yaml
ENV BIOBOX_EXEC  assemble
