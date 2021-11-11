FROM narima/base:bull

ENV DEBIAN_FRONTEND noninteractive

# add Experimental Package & Install Google Chrome
ADD https://raw.githubusercontent.com/Ncode2014/nekadok/req/requirements.txt requirements.txt
RUN set -ex \
    && echo deb http://http.us.debian.org/debian/ testing non-free contrib main > /etc/apt/sources.list \
    && apt-get -qq update \
    && apt-get -qq -y install --no-install-recommends \
        apt-utils \
        aria2 \
        bash \
        build-essential \
        curl \
        figlet \
        git \
        gnupg2 \
        jq \
        libpq-dev \
        libssl-dev \
        libwebp6 \
        libxml2 \
        neofetch \
        postgresql \
        pv \
        sudo \
        unar \
        unrar-free \
        unzip \
        wget \
        xz-utils \
        zip \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \

    && apt-get -qq update \
    && apt-get -qq -y install google-chrome-beta \ 
    && apt-get -qq update \

    # Install chromedriver
    && wget -N https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_96)/chromedriver_linux64.zip -P ~/ \
    && unzip ~/chromedriver_linux64.zip -d ~/ \
    && rm ~/chromedriver_linux64.zip \
    && mv -f ~/chromedriver /usr/bin/chromedriver \
    && chown root:root /usr/bin/chromedriver \
    && chmod 0755 /usr/bin/chromedriver \

    # Install Python modules
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt --use-feature=2020-resolver \
    && rm -f requirements.txt \
    && pip3 install gdown \
    && pip3 cache purge \

    # a simple way to catch some dependencies
    # for a note
    # https://megatools.megous.com/
    # https://www.rarlab.com/
    && mkdir -p /tmp/ \
    && cd /tmp/ \
    && gdown --id 1yICNR7-1HHmdqPtwnmzeg4DzGZ-MohtM -O /tmp/nekadok.tar.gz \
    && tar -xzvf nekadok.tar.gz \
    && cd nekadok \
    && cp -v rar unrar ffmpeg megatools ffprobe /usr/bin \
    && cp -v rarfiles.lst /etc && cp -v default.sfx /usr/lib \
    && chmod +x /usr/bin/ffmpeg /usr/bin/rar /usr/bin/unrar /usr/bin/megatools /usr/bin/ffprobe \
    && rm -rf nekadok \
    && rm -f nekadok.tar.gz \

    # Cleanup
    && apt-get -qq -y purge --auto-remove \
        apt-utils \
        build-essential \
        gnupg2 \
    && apt-get -qq -y clean \
    && rm -r /tmp/* \
    && rm -rf -- /var/lib/apt/lists/* /home/* /var/cache/apt/archives/* /etc/apt/sources.list.d/*

EXPOSE 80 443

CMD ["python3"]
