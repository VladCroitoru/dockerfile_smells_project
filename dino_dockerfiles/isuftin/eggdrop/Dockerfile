FROM ubuntu:14.04

MAINTAINER Ivan Suftin <isuftin@gmail.com>

USER "root"

VOLUME ["/scripts", "/modules", "/files", "/logs", "/files/incoming", "/configs", "/modules", "/docker-egg-init.d"]

ENV eggdrop_user="eggdrop"

RUN useradd -m ${eggdrop_user} -U 

WORKDIR "/tmp"

# Install Dependencies

COPY /scripts/install-dependencies.sh install-dependencies.sh

RUN chmod a+x install-dependencies.sh && sleep 1 && ./install-dependencies.sh;

# Copy compile and configuration files 

WORKDIR "/home/${eggdrop_user}"

COPY /scripts/compile-eggdrop.sh compile-eggdrop.sh

COPY /scripts/configure-eggdrop.sh configure-eggdrop.sh

RUN chown -R ${eggdrop_user}:${eggdrop_user} /scripts && \
    chown -R ${eggdrop_user}:${eggdrop_user} /modules && \
    chown -R ${eggdrop_user}:${eggdrop_user} /files && \
    chown -R ${eggdrop_user}:${eggdrop_user} /configs && \
    chown -R ${eggdrop_user}:${eggdrop_user} /modules && \
    chown ${eggdrop_user}:${eggdrop_user} compile-eggdrop.sh && \
    chown ${eggdrop_user}:${eggdrop_user} configure-eggdrop.sh && \
    chmod a+x compile-eggdrop.sh && \
    chmod a+x configure-eggdrop.sh

# Compile Eggdrop

USER "${eggdrop_user}"

RUN ./compile-eggdrop.sh

# Configure Eggdrop

ENV listen_ports="8001|all"

ENV owner="myself"

ENV eggdrop_nickname="testbot"

ENV PATH ${PWD}:$PATH

# Start the eggdrop bot

COPY /scripts/eggdrop-entrypoint.sh eggdrop-entrypoint.sh

ENTRYPOINT ["eggdrop-entrypoint.sh"]
CMD ["eggdrop", "-n", "eggdrop.conf"]
