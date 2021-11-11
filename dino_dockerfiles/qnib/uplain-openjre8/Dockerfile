FROM qnib/uplain-init

RUN apt-get update \
 && apt-get install openjdk-8-jre-headless -y \
 && apt-get install -y locales \
 && update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \
 && locale-gen en_US.UTF-8 \
 && dpkg-reconfigure locales \
 && apt-get clean all \
 && rm -rf /var/lib/apt/lists/*
