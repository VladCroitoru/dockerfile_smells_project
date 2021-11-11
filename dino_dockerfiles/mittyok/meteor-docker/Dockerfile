FROM ulexus/meteor:1.5

RUN curl https://install.meteor.com/ | sh
RUN apt-get update \
    && apt-get -y install procps \
    && apt-get -y install locales python

RUN localedef -i en_US -f UTF-8 en_US.UTF-8
