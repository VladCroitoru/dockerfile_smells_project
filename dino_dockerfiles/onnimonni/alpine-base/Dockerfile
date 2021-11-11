FROM alpine
MAINTAINER onni@keksi.io

# Build arguments
ARG S6_OVERLAY_VERSION=v1.18.1.3

# Finland is quite nice place to live.
# Instead of forking this you should move your living address here.
ENV TZ="Europe/Helsinki"

RUN set -x \

    # This folder is in $PATH by default but isn't created by default
    && mkdir -p /usr/local/sbin \
    && cd /usr/local/sbin \

    # Add more repositories for our convenience
    && echo http://dl-cdn.alpinelinux.org/alpine/edge/main | tee /etc/apk/repositories \
    && echo @testing http://dl-cdn.alpinelinux.org/alpine/edge/testing | tee -a /etc/apk/repositories \
    && echo @community http://dl-cdn.alpinelinux.org/alpine/edge/community | tee -a /etc/apk/repositories \

    # Update openssl to fix: wget: can't execute 'ssl_helper': No such file or directory
    && apk add --update openssl \

    # Install sha256sum validator to check that we download the right files
    && wget -q -O validate_sha256sum https://gist.githubusercontent.com/onnimonni/b49779ebc96216771a6be3de46449fa1/raw/d3ef37ab4a653e1b7655df55dfeadd54e0bacf84/validate_sha256sum \
    # This is semi meta but validate that our validator is valid
    && sha256sum validate_sha256sum | grep 0f7b790036f7cd00610cbe9e79c5b6b42d5b0e02beaff9549bdc43fc99910709 \
    && echo "Success: validate_sha256sum matches provided sha256sum" || exit 1 \
    && chmod +x validate_sha256sum \

    # apk helper from progrium
    && wget -q -O apk-install https://raw.githubusercontent.com/gliderlabs/docker-alpine/master/builder/scripts/apk-install \
    && validate_sha256sum apk-install f5f10018cba8440e4317b5559665693e5ecf922592b50d20a1c65a8c2f5fd5ab \

    # Nice owner helper from colstrom
    && wget -q -O owner https://raw.githubusercontent.com/colstrom/owner/master/bin/owner \
    && validate_sha256sum owner e2c69e2742caa88bc1afb8e4575a312f21a9021461d0b5961f9204dc2f630520 \

    # Give execution rights to all scripts which we downloaded
    && chmod a+x * \

    ##
    # Add S6-overlay to use S6 process manager
    # source: https://github.com/just-containers/s6-overlay/#the-docker-way
    ##
    && wget -q -O /tmp/s6-overlay-amd64.tar.gz https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    && validate_sha256sum /tmp/s6-overlay-amd64.tar.gz 5bb2c67db9369494578e0205fdcf6f44011a1913b98abbc6a7aac551a7c1b0a8 \
    && tar -zxvf /tmp/s6-overlay-amd64.tar.gz -C / \

    # Add default timezone
    && apk add tzdata \
    && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone \

    # Install envsubst command for replacing config files in system startup
    # - it needs libintl package
    # - only weights 100KB combined with it's libraries
    && apk add gettext libintl \
    && mv /usr/bin/envsubst /usr/local/sbin/envsubst \

    # Install drill - dig alternative from freebsd
    # - This is for debugging dns based load balancing which super popular in clusters
    && apk add drill \
    # Symlink into dig for convenience
    && ln -s /usr/bin/drill /usr/local/sbin/dig \

    ##
    # Create a few aliases
    # - I didn't figure out how to load aliases into sh shell with docker so we add scripts instead
    ##

    # ll
    && echo -e "#!/bin/sh \nls -lah \"\$@\"" > /usr/local/bin/ll \
    # la
    && echo -e "#!/bin/sh \nls -A \"\$@\"" > /usr/local/bin/la \
    # l
    && echo -e "#!/bin/sh \nls -CF \"\$@\"" > /usr/local/bin/l \

    && chmod a+x /usr/local/bin/* \

    # Cleanup
    && apk del openssl tzdata gettext \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

ENTRYPOINT ["/init"]
