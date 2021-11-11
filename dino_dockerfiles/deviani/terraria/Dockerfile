FROM debian:8

MAINTAINER Emil Haugbergsmyr <emil@raeven.net>

VOLUME ["/world", "/config", "/logs"]

ENV WORLD_NAME docker
ENV WORLD_SIZE 3
ENV MAX_PLAYERS 16
ENV IP 0.0.0.0
ENV PORT 7777

# Add mono repository and update os and install required applications
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list && \
    echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list && \
    apt-get update && apt-get upgrade -y && \
    apt-get install -yf zip mono-runtime mono-devel supervisor curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install confd
RUN curl -qL https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-amd64 -o /confd && chmod +x /confd && \
    mkdir -p /etc/confd/{conf.d,templates}

# Download and install TShock software
ADD https://github.com/Pryaxis/TShock/releases/download/v4.5.4/TShock4.5.4_Terraria1.4.2.3.zip /
RUN unzip TShock4.5.4_Terraria1.4.2.3.zip -d /tshock && \
    rm TShock4.5.4_Terraria1.4.2.3.zip

COPY supervisord.tmpl /etc/confd/templates/supervisord.tmpl
COPY supervisord.toml /etc/confd/conf.d/supervisord.toml

ADD run.sh /
RUN chmod u+x /run.sh

EXPOSE 7777

CMD ["/run.sh"]
