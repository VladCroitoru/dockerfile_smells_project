FROM debian:jessie

ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 /usr/local/bin/dumb-init

RUN set -x \
    # Install qBittorrent-NoX
    && apt-get update \
    && apt-get install -y qbittorrent-nox \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

    # Add non-root user
    && useradd --system --uid 520 -m --shell /usr/sbin/nologin qbittorrent \

    # Create symbolic links to simplify mounting
    && mkdir -p /home/qbittorrent/.config/qBittorrent \
    && chown qbittorrent:qbittorrent /home/qbittorrent/.config/qBittorrent \
    && ln -s /home/qbittorrent/.config/qBittorrent /config \

    && mkdir -p /home/qbittorrent/.local/share/data/qBittorrent \
    && chown qbittorrent:qbittorrent /home/qbittorrent/.local/share/data/qBittorrent \
    && ln -s /home/qbittorrent/.local/share/data/qBittorrent /torrents \

    && mkdir /downloads \
    && chown qbittorrent:qbittorrent /downloads \

    # https://github.com/Yelp/dumb-init
    && chmod +x /usr/local/bin/dumb-init


# Default configuration file.
COPY qBittorrent.conf /default/qBittorrent.conf
COPY entrypoint.sh /

VOLUME ["/config", "/torrents", "/downloads"]

EXPOSE 8080 6881

USER qbittorrent

ENTRYPOINT ["dumb-init", "/entrypoint.sh"]
CMD ["qbittorrent-nox"]
