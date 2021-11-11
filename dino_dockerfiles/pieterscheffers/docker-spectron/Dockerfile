FROM node:slim

RUN apt-get update \
  && apt-get install -y \
    g++-multilib \
    lib32z1 \
    lib32ncurses5 \
    rpm \
    fakeroot \
    dpkg \
    libdbus-1-dev \
    libx11-dev \
    libavahi-compat-libdnssd-dev \
    g++ \
    gcc-4.8-multilib \
    g++-4.8-multilib \
    libgtk2.0-0 \
    libgtk2.0-dev \
    xvfb \
    libxtst6 \
    libxss1 \
    libnss3 \
    libasound2 \
    libgconf-2-4 \
  && rm -rf /var/lib/apt/lists/*

ENV ELECTRON_ENABLE_STACK_DUMPING=true
ENV ELECTRON_ENABLE_LOGGING=true
ENV DISPLAY=:99

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
