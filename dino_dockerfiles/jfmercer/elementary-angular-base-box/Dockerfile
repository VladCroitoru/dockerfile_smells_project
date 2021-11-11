FROM jfmercer/yarn:8.1.0

MAINTAINER John F. Mercer <john.f.mercer@gmail.com>

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee -a /etc/apt/sources.list; \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -; \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    libxpm4 \
    libxrender1 \
    libgtk2.0-0 \
    libnss3 \
    libgconf-2-4 \
    gtk2-engines-pixbuf \
    xfonts-cyrillic \
    xfonts-100dpi \
    xfonts-75dpi \
    xfonts-base \
    xfonts-scalable \
    xvfb \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY :99
ENV CHROME_BIN /usr/bin/chromium

COPY xvfb-setup.sh /usr/local/bin
RUN chmod a+x /usr/local/bin/xvfb-setup.sh
