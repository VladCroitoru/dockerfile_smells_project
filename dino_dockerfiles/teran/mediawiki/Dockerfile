FROM teran/php7-fpm@sha256:11cb7fdf6790e0a89559f3337d3765472cb9e4e0c3b249d759ae96b3b43b5cde

ARG major=1.32
ARG minor=2

LABEL application=mediawiki
LABEL version=${major}.${minor}
LABEL description="Mediawiki==${major}.${minor} with nginx and php7-fpm"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && \
    apt-get install -y --no-install-suggests --no-install-recommends \
        curl=7.58.0-2ubuntu3.7 && \
    apt-get clean && \
    rm -rvf /var/lib/apt/lists/*

RUN gpg --fetch-keys "https://www.mediawiki.org/keys/keys.txt"

RUN curl -sfo /tmp/mediawiki.tgz https://releases.wikimedia.org/mediawiki/${major}/mediawiki-${major}.${minor}.tar.gz && \
    curl -sfo /tmp/mediawiki.sig https://releases.wikimedia.org/mediawiki/${major}/mediawiki-${major}.${minor}.tar.gz.sig && \
    gpg --verify /tmp/mediawiki.sig /tmp/mediawiki.tgz && \
    mkdir -p /var/www && \
    tar xzf /tmp/mediawiki.tgz -C /tmp && \
    cp -r /tmp/mediawiki*/* /var/www/ && \
    rm -rf /tmp/mediawiki*
COPY --chown=root:root nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
