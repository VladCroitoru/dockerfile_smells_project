FROM debian:jessie
MAINTAINER Carlo Bellettini

RUN apt-get update && apt-get -y install curl bzip2 make gcc
RUN curl -L https://ftp.eiffel.com/pub/download/15.08/Eiffel_15.08_gpl_97862-linux-x86-64.tar.bz2 | tar xj -C /usr/local


RUN apt-get install -y libxtst-dev libgtk2.0-dev

ENV ISE_EIFFEL /usr/local/Eiffel_15.08
ENV ISE_PLATFORM linux-x86-64
ENV ISE_LIBRARY $ISE_EIFFEL
ENV EIFFEL_LIBRARY /eiffel
ENV PATH $PATH:$ISE_EIFFEL/studio/spec/$ISE_PLATFORM/bin

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/eiffel && \
    echo "eiffel:x:${uid}:${gid}:eiffel,,,:/home/eiffel:/bin/bash" >> /etc/passwd && \
    echo "eiffel:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/eiffel

USER eiffel
ENV HOME /home/eiffel
CMD estudio
