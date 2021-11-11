FROM ubuntu:15.10

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 575159689BEFB442 && \
    echo 'deb http://download.fpcomplete.com/ubuntu vivid main' >/etc/apt/sources.list.d/fpco.list && \
    apt-get update && apt-get install stack -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD setup-stack-env /usr/bin/
RUN /usr/bin/setup-stack-env lts-3
RUN /usr/bin/setup-stack-env lts-4
RUN /usr/bin/setup-stack-env nightly
