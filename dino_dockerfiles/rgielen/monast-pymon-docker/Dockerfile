FROM ubuntu:17.10
MAINTAINER "Rene Gielen" <rgielen@apache.org>

RUN apt-get update && apt-get -y install python python-twisted python-zope.interface python-pip wget unzip gettext-base \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && rm -rf /tmp/*

# RUN wget https://downloads.sourceforge.net/project/basicproperty/basicproperty/0.6.12a/basicproperty-0.6.12a.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fbasicproperty%2Ffiles%2F&ts=1500908704&use_mirror=netcologne
RUN wget https://downloads.sourceforge.net/project/basicproperty/basicproperty/0.6.12a/basicproperty-0.6.12a.tar.gz \
        && tar -xzf basicproperty-0.6.12a.tar.gz \
        && cd basicproperty-0.6.12a \
        && python setup.py install \
        && cd .. \
        && rm basicproperty-0.6.12a.tar.gz \
        && rm -rf basicproperty-0.6.12a

RUN wget https://downloads.sourceforge.net/project/starpy/starpy/1.0.0a13/starpy-1.0.0a13.tar.gz \
        && tar -xzf starpy-1.0.0a13.tar.gz \
        && cd starpy-1.0.0a13 \
        && python setup.py install \
        && cd .. \
        && rm starpy-1.0.0a13.tar.gz \
        && rm -rf starpy-1.0.0a13

RUN wget https://github.com/dagmoller/monast/archive/master.zip \
        && unzip master.zip \
        && mv monast-master/pymon / \
        && rm -rf monast-master \
        && echo "$PWD" \
        && rm master.zip

RUN groupadd -r monast && useradd -r -g monast monast && mkdir /pymon/config && chown monast.monast /pymon/config

ADD monast.conf.template /pymon/
ADD configure-and-start.sh /pymon/
# VOLUME /pymon/config

ENV BIND_HOST=0.0.0.0
ENV BIND_PORT=5039
ENV ASTERISK_HOST=localhost
ENV ASTERISK_PORT=5038
ENV AMI_USERNAME=admin
ENV AMI_PASSWORD=admin
ENV DEFAULT_CONTEXT=default
ENV TRANSFER_CONTEXT=default
ENV MEETME_CONTEXT=default
ENV USER_ADMIN_SECRET=admin
ENV USER_AGENT_SECRET=agent
ENV ADDITIONAL_CONFIG_LINES=""

EXPOSE ${BIND_PORT}

USER monast

ENTRYPOINT ["/pymon/configure-and-start.sh"]
