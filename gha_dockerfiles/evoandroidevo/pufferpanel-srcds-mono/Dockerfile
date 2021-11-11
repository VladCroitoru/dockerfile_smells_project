FROM golang:bullseye AS builder

ARG tags=none
ARG version=devel
ARG sha=devel

ENV CGOENABLED=1

RUN apt update
RUN apt upgrade -y
RUN go version && \
    apt install -y gcc musl-dev git curl nodejs npm make gcc g++ python2

WORKDIR /build
#WORKDIR /build/pufferpanel
RUN git clone https://github.com/PufferPanel/PufferPanel.git
WORKDIR /build/PufferPanel
#COPY . .
RUN go build -v -tags $tags -ldflags "-X 'github.com/pufferpanel/pufferpanel/v2.Hash=$sha' -X 'github.com/pufferpanel/pufferpanel/v2.Version=$version'" -o /pufferpanel/pufferpanel github.com/pufferpanel/pufferpanel/v2/cmd && \
    mv assets/email /pufferpanel/email && \
    cd client && \
    npm install && \
    npm run dev-build && \
    mv dist /pufferpanel/www/

FROM steamcmd/steamcmd:ubuntu-18 as srcdsbuilder
ENV USER root
ENV HOME /root/installer
WORKDIR $HOME
RUN apt-get update && apt-get install -y --no-install-recommends curl tar
RUN curl -fsSL https://media.steampowered.com/installer/steamcmd_linux.tar.gz --output steamcmd.tar.gz
RUN tar -xvzf steamcmd.tar.gz && rm steamcmd.tar.gz

FROM mono as base
COPY --from=builder /pufferpanel /pufferpanel

EXPOSE 8080 5657
RUN mkdir -p /etc/pufferpanel && \
    mkdir -p /var/lib/pufferpanel

COPY --from=srcdsbuilder /lib/i386-linux-gnu /lib/
COPY --from=srcdsbuilder /root/installer/linux32/libstdc++.so.6 /lib/
COPY --from=srcdsbuilder /root/installer/steamcmd.sh /usr/lib/games/steam/
COPY --from=srcdsbuilder /root/installer/linux32/steamcmd /usr/lib/games/steam/
COPY --from=srcdsbuilder /usr/games/steamcmd /usr/bin/steamcmd

RUN apt update
RUN apt upgrade -y
#RUN apt install gnupg ca-certificates
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
#RUN echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | tee /etc/apt/sources.list.d/mono-official-stable.list
#RUN apt update
#RUN apt install mono-complete

ENV PUFFER_LOGS=/etc/pufferpanel/logs \
    PUFFER_WEB_HOST=0.0.0.0:8080 \
    PUFFER_PANEL_DATABASE_SESSION=60 \
    PUFFER_PANEL_DATABASE_DIALECT=sqlite3 \
    PUFFER_PANEL_DATABASE_URL="file:/etc/pufferpanel/pufferpanel.db?cache=shared" \
    PUFFER_PANEL_DATABASE_LOG=false \
    PUFFER_PANEL_TOKEN_PRIVATE=/etc/pufferpanel/private.pem \
    PUFFER_PANEL_WEB_FILES=/pufferpanel/www \
    PUFFER_PANEL_EMAIL_TEMPLATES=/pufferpanel/email/emails.json \
    PUFFER_PANEL_EMAIL_PROVIDER=debug \
    PUFFER_PANEL_SETTINGS_COMPANYNAME=PufferPanel \
    PUFFER_PANEL_SETTINGS_MASTERURL=http://localhost:8080 \
    PUFFER_DAEMON_CONSOLE_BUFFER=50 \
    PUFFER_DAEMON_CONSOLE_FORWARD=false \
    PUFFER_DAEMON_SFTP_HOST=0.0.0.0:5657 \
    PUFFER_DAEMON_SFTP_KEY=/etc/pufferpanel/sftp.key \
    PUFFER_DAEMON_AUTH_URL=http://localhost:8080 \
    PUFFER_DAEMON_AUTH_CLIENTID=none \
    PUFFER_DAEMON_DATA_CACHE=/var/lib/pufferpanel/cache \
    PUFFER_DAEMON_DATA_SERVERS=/var/lib/pufferpanel/servers \
    PUFFER_DAEMON_DATA_MODULES=/var/lib/pufferpanel/modules \
    PUFFER_DAEMON_DATA_CRASHLIMIT=3

WORKDIR /pufferpanel

ENTRYPOINT ["/pufferpanel/pufferpanel"]
CMD ["run"]