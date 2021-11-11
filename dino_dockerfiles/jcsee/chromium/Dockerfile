FROM ubuntu:16.04
ENV DEBIAN_FRONTEND=noninteractive \
    USERNAME=chromium \
    HOME=/home/chromium

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      ca-certificates \
      chromium-browser \
      chromium-browser-l10n \
      hicolor-icon-theme \
      fonts-arphic-bkai00mp \
      fonts-arphic-bsmi00lp \
      fonts-arphic-gbsn00lp \
      fonts-arphic-gkai00mp \
      fonts-opensymbol \
 && rm -rf /var/lib/apt/lists/* \
 && useradd --uid 1000 --no-create-home --home-dir $HOME $USERNAME \
 && mkdir $HOME /data /Cache \
 && chown -R chromium:chromium $HOME /data /Cache

COPY local.conf /etc/fonts/local.conf
USER $USERNAME
WORKDIR $HOME
