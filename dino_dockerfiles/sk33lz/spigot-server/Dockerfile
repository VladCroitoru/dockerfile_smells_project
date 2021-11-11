FROM dlord/spigot
MAINTAINER Jason Moore sk33lz@gmail.com

RUN wget -qO- https://github.com/Tiiffi/mcrcon/releases/download/v0.0.5/mcrcon-0.0.5-linux-x86-64.tar.gz | tar xvz -C /tmp && \
    cp /tmp/mcrcon /usr/local/bin/mcrcon && \
    rm -Rf /tmp/*


COPY spigot /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/spigot"]
CMD ["run"]
