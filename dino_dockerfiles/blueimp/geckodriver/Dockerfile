#
# Geckodriver Dockerfile
#

FROM blueimp/basedriver

# Install the latest version of Firefox:
RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
    # Firefox dependencies:
    libgtk-3-0 \
    libdbus-glib-1-2 \
    # Bzip2 to extract the Firefox tarball:
    bzip2 \
    # Reverse proxy for geckodriver:
    nginx \
  && DL='https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64' \
  && curl -sL "$DL" | tar -xj -C /opt \
  && ln -s /opt/firefox/firefox /usr/local/bin/ \
  # Remove obsolete files:
  && apt-get autoremove --purge -y \
    bzip2 \
  && apt-get clean \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# Install the latest version of Geckodriver:
RUN BASE_URL=https://github.com/mozilla/geckodriver/releases/download \
  && VERSION=$(curl -sL \
    https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
    grep tag_name | cut -d '"' -f 4) \
  && curl -sL "$BASE_URL/$VERSION/geckodriver-$VERSION-linux64.tar.gz" | \
    tar -xz -C /usr/local/bin

# Configure nginx to run in a container context:
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
RUN chown -R webdriver:webdriver /var/lib/nginx
RUN touch /run/nginx.pid && chown -R webdriver:webdriver /run/nginx.pid

COPY nginx.conf /etc/nginx/
COPY reverse-proxy.sh /usr/local/bin/reverse-proxy

USER webdriver

ENTRYPOINT ["entrypoint", "reverse-proxy", "geckodriver"]

# Bind geckodriver to port 5555:
CMD ["--port", "5555"]

# Expose nginx on port 4444, forwarding to geckodriver on port 5555:
EXPOSE 4444
