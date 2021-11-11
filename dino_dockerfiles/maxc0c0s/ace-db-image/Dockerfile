FROM mysql

RUN apt-get -y update && apt-get install -y git
# TODO Use the upstream repo once git@github.com:maxc0c0s/ace-db-image.git is merged.
RUN git clone https://github.com/maxc0c0s/ACE.git /tmp/ACE

COPY  build_database_init.sh /tmp/
RUN /tmp/build_database_init.sh
