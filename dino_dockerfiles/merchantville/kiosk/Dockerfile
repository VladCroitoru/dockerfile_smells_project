FROM alpine:3.3

ENV FIREFOX_VERSION="38.3.0" \
    FIREFOX_ADDONS_URL="https://addons.mozilla.org/firefox/downloads/latest" \
    EXT_UID="207605"

WORKDIR /scratch

# Install required software and font packages
RUN apk add --update bash curl dbus-x11 libcanberra-gtk2 firefox=${FIREFOX_VERSION}-r1 && \
    apk add xdotool --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \
    export TTFS=$(apk search -q ttf- | grep -v '\-doc') && \
    export FONTS=$(apk search -q font- | grep -v '\-doc') && \
    apk add ${TTFS} ${FONTS} && \
    rm -rf /var/cache/apk/*

# Install tabrotating plugin
RUN curl -LO $FIREFOX_ADDONS_URL/$EXT_UID/addon-${EXT_UID}-latest.xpi && \
    unzip addon-${EXT_UID}-latest.xpi && \
    rm addon-${EXT_UID}-latest.xpi && \
    export EXT_ID=$(cat install.rdf | grep "<em:id>" | head -n 1 | sed 's/^.*>\(.*\)<.*$/\1/g') && \
    export EXT_DIR="/usr/lib/firefox-${FIREFOX_VERSION}/browser/extensions/${EXT_ID}" && \
    export EXT_PATH="Extension0=${EXT_DIR}^M" && \
    mkdir ${EXT_DIR} && mv * ${EXT_DIR}

# Setup Firefox user profile
COPY assets/prefs.js /usr/lib/firefox-38.3.0/browser/extensions/tabrotator@davidfichtmueller.de/defaults/preferences/prefs.js
COPY assets/mozilla/firefox /root/.mozilla/firefox/
COPY assets/urls.txt /assets/urls.txt

ENTRYPOINT exec firefox $(cat /assets/urls.txt)
