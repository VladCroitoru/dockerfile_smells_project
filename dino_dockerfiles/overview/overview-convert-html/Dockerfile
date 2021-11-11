# Debian, not Alpine, gives the best trade-offs:
#
# * Official Firefox binaries are built against libc.
# * Debian has a great selection of fonts. (When converting, fonts are rarely
#   embedded in the HTML. If we have the font on our system, we can embed
#   anyway instead of defaulting to a boring font.)
FROM debian:stretch-slim AS os

RUN sed -i -e 's/stretch main$/stretch main contrib/' /etc/apt/sources.list \
  && apt-get update \
  && apt-get install --no-install-recommends -y \
    ca-certificates \
    curl \
    bzip2 \
    gpg \
    xz-utils \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    fonts-arphic-ukai \
    fonts-arphic-uming \
    fonts-dejavu \
    fonts-font-awesome \
    fonts-ipafont-gothic \
    fonts-ipafont-mincho \
    fonts-nanum \
    fonts-noto \
    fonts-noto-cjk \
    fonts-noto-mono \
    ttf-mscorefonts-installer \
    jq \
    poppler-utils \
  && curl -o /sbin/tini https://github.com/krallin/tini/releases/download/v0.17.0/tini-amd64 \
  && chmod +x /sbin/tini \
  && curl -o /tmp/fonts-open-sans.deb http://http.us.debian.org/debian/pool/main/f/fonts-open-sans/fonts-open-sans_1.11-1_all.deb \
  && dpkg -i /tmp/fonts-open-sans.deb \
  && rm -f /tmp/fonts-open-sans.deb \
  && apt-get clean -y \
  && rm -rf /var/cache/debconf/* /var/lib/apt/lists/* /var/log/* /tmp/* /var/tmp/*

# Install Firefox. (Debian provides firefox-esr, which is too old for SlimerJS.)
RUN curl -o - --location https://download-installer.cdn.mozilla.net/pub/firefox/releases/60.0.1/linux-x86_64/en-US/firefox-60.0.1.tar.bz2 \
        | tar -xj -C / \
   && mkdir -p /opt \
   && mv /firefox /opt/
# Install SlimerJS
RUN curl -o - --location https://github.com/adamhooper/slimerjs/releases/download/stripped-to-the-minimum.001/slimerjs-1.1.0-pre.tar.bz2 \
        | tar -xj -C / \
    && mkdir -p /opt \
    && mv /slimerjs-1.* /opt/slimerjs
# Put them in the PATH
ENV PATH /opt/firefox:/opt/slimerjs:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

# Install Ted, for converting RTF
ENV TED_VERSION 2.23
RUN true \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    libgtk2.0-0 \
    libjpeg62-turbo \
    libpaper1 \
    libpcre3 \
    libpng16-16 \
    libtiff5 \
    libx11-6 \
    libxft2 \
    libxpm4 \
    zlib1g \
    ghostscript \
    xvfb \
    build-essential \
    pkgconf \
    libgtk2.0-dev \
    libjpeg62-turbo-dev \
    libpaper-dev  \
    libpcre3-dev \
    libpng-dev \
    libtiff5-dev \
    libx11-dev \
    libxft-dev \
    libxpm-dev \
    zlib1g-dev \
  && mkdir /build \
  && curl -o - --location https://ftp.nluug.nl/pub/editors/ted/ted-2.23.src.tar.gz \
        | tar -C /build -zxf - \
  && cd /build/Ted-${TED_VERSION} \
  && ln -sf /usr/lib/x86_64-linux-gnu/pkgconfig/libtiff-4.pc /usr/lib/x86_64-linux-gnu/pkgconfig/libtiff.pc \
  && make -j4 install \
  && rm -f /usr/lib/x86_64-linux-gnu/pkgconfig/libtiff.pc \
  && cd / \
  && rm -rf /build \
  && apt-get remove -y --purge \
    build-essential \
    pkgconf \
    libgtk2.0-dev \
    libjpeg62-turbo-dev \
    libpaper-dev \
    libpcre3-dev \
    libpng-dev \
    libtiff5-dev \
    libx11-dev \
    libxft-dev \
    libxpm-dev \
    zlib1g-dev \
  && apt-get autoremove -y --purge \
  && apt-get clean -y \
  && rm -rf /var/cache/debconf/* /var/lib/apt/lists/* /var/log/* /tmp/* /var/tmp/*


FROM overview/overview-convert-framework:0.0.16 AS framework


FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/run
COPY --from=framework /app/convert-single-file /app/convert
COPY do-convert-single-file convert.js /app/
CMD [ "/app/run" ]


FROM base AS test
COPY --from=framework /app/test-convert-single-file /app/
COPY test/ /app/test/
RUN [ "/app/test-convert-single-file" ]
CMD [ "true" ]


FROM base AS production
