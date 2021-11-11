FROM debian:9

ARG DEADLINE_INSTALLER

ADD $DEADLINE_INSTALLER .
RUN apt-get update && apt-get install -y bzip2 &&\
    ./DeadlineClient-*.run \
    --mode unattended --repositorydir /repo && \
    rm -f ./DeadlineClient-*.run
CMD ["/opt/Thinkbox/Deadline10/bin/deadlinelauncher", "-nogui", "-slave"]