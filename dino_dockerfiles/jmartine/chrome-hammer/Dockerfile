FROM debian:sid

ADD  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb /src/google-chrome-stable_current_amd64.deb
COPY start-chrome /start-chrome

RUN mkdir -p /usr/share/icons/hicolor && \
    apt-get update && apt-get install -y \
    ca-certificates \
    gconf-service \
    hicolor-icon-theme \
    libappindicator1 \
    libasound2 \
    libcanberra-gtk-module \
    libcurl3 \
    libexif-dev \
    libgconf-2-4 \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    libnspr4 \
    libnss3 \
    libpango1.0-0 \
    libv4l-0 \
    libxss1 \
    libxtst6 \
    xauth \
    xdg-utils \
    xvfb \
    wget \
    --no-install-recommends && \
    dpkg -i '/src/google-chrome-stable_current_amd64.deb' && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "/start-chrome" ]
