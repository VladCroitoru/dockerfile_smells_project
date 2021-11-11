FROM ubuntu
MAINTAINER Kyle Manna <kyle@kylemanna.com>

ARG USER_ID
ARG GROUP_ID

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN wget https://bintray.com/artifact/download/omni/OmniBinaries/omnicore-0.0.11.2-rel-linux64.tar.gz && echo "787e5fef50118f59d76128d3a8435efc355b3a18962c3e209a79556e47a48ec4  omnicore-0.0.11.2-rel-linux64.tar.gz" | sha256sum --status -c && tar -xzf omnicore-0.0.11.2-rel-linux64.tar.gz && cp -R omnicore-0.0.11.2-rel/* /usr/


ENV HOME /bitcoin

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}
RUN groupadd -g ${GROUP_ID} bitcoin
RUN useradd -u ${USER_ID} -g bitcoin -s /bin/bash -m -d /bitcoin bitcoin

RUN chown bitcoin:bitcoin -R /bitcoin

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

USER bitcoin

VOLUME ["/bitcoin"]

EXPOSE 8332 8333 18332 18333

WORKDIR /bitcoin

CMD ["omni_oneshot"]

