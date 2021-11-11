FROM node:wheezy
MAINTAINER Jay Luker <lbjay@reallywow.com>

RUN groupadd -r anonuser -g 433 && \
    adduser --uid 431 --system --gid 433 --home /opt/anon --shell /sbin/nologin anonuser && \
    adduser anonuser sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /opt/anon
RUN git clone https://github.com/edsu/anon.git

WORKDIR /opt/anon/anon
RUN npm install

COPY run.sh ./run.sh
RUN chmod 755 ./run.sh
RUN chown -R anonuser:anonuser .
USER anonuser

ENTRYPOINT ["/opt/anon/anon/run.sh"]

CMD []
