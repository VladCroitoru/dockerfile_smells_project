FROM perl:5.20
MAINTAINER = Daniel Gempesaw <gempesaw@gmail.com>

# get standalone server
RUN mkdir -p /opt/selenium && \
    wget --no-verbose https://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.0.jar \
         -O /opt/selenium/selenium-server-standalone.jar

# get google-chrome-stable, via https://github.com/jfrazelle/dockerfiles/blob/5a6ef53d6ae45f4dd568dff4dbe5789af990e26c/chrome/stable/Dockerfile
RUN apt-get clean && apt-get update && \
    echo 'deb http://httpredir.debian.org/debian testing main' >> /etc/apt/sources.list && \
    apt-get install -y \
    ca-certificates \
    curl \
    hicolor-icon-theme \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    libv4l-0 \
    --no-install-recommends \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends

# get chromedriver
RUN apt-get install -y unzip && \
    wget -N http://chromedriver.storage.googleapis.com/2.21/chromedriver_linux64.zip -P ~/Downloads && \
    unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads && \
    chmod +x ~/Downloads/chromedriver && \
    mv -f ~/Downloads/chromedriver /usr/local/bin/chromedriver && \
    rm ~/Downloads/chromedriver_linux64.zip

# libpcsclite1 keeps failing when being installed automatically, doing
# it explicitly seems to help.
RUN apt-get install -y libpcsclite1 && \
    apt-get install -y iceweasel && \
    apt-get install -y openjdk-7-jre && \
    apt-get install -y xvfb && \
    apt-get install -y phantomjs
ENV DISPLAY=:1

# clean up package manager, get the newest version of SRD with deps
RUN rm -rf /var/lib/apt/lists/* && \
    git config --global user.name "docker" && \
    git config --global user.email "docker@example.com" && \

    cpanm --notest --quiet Dist::Zilla && \
    cpanm --notest --quiet --installdeps Selenium::Remote::Driver && \
    mkdir -p /opt/Selenium-Remote-Driver

WORKDIR /opt/Selenium-Remote-Driver
RUN SHA=05acd53 git clone https://github.com/gempesaw/Selenium-Remote-Driver /opt/Selenium-Remote-Driver && \
    dzil authordeps --missing | xargs -n 5 -P 10 cpanm --notest --quiet && \
    dzil listdeps   --missing | xargs -n 5 -P 10 cpanm --notest --quiet

COPY start.sh /root/start.sh

ENTRYPOINT ["/bin/bash", "/root/start.sh"]
