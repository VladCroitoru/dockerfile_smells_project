FROM debian:sid-slim

RUN export DEBIAN_FRONTEND=noninteractive && \
  export VNC_ENABLED=true && \
  export EXPOSE_X11=true

RUN apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install --no-install-recommends --no-install-suggests -y \
    xvfb \
    xauth \
    ca-certificates \
    x11vnc \
    fluxbox \
    curl \
    firefox \
 && rm -fr /var/lib/apt/lists/* \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && export TINI_VERSION=v0.14.0 \
 && curl -sL https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini > /sbin/tini \
 && chmod +x /sbin/tini

RUN sed -i 's/LISTENTCP=""/LISTENTCP="-listen tcp"/' /usr/bin/xvfb-run

WORKDIR /app

COPY entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
COPY vnc-start.sh /usr/local/bin/vnc-start
RUN chmod +x /usr/local/bin/vnc-start

# Configure Xvfb via environment variables:
ENV SCREEN_WIDTH 1440
ENV SCREEN_HEIGHT 900
ENV SCREEN_DEPTH 24
ENV DISPLAY :60

ENTRYPOINT ["entrypoint"]

# Expose the default webdriver port:
EXPOSE 4444
EXPOSE 2828
EXPOSE 5900

CMD ["geckodriver", "--host", "0.0.0.0"]