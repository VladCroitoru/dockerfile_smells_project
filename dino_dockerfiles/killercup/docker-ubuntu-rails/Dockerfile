FROM ubuntu:14.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:kirillshkrogalev/ffmpeg-next \
    && apt-add-repository ppa:brightbox/ruby-ng \
    && add-apt-repository ppa:chris-lea/node.js \
    && apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y --no-install-recommends \
        git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev libmysqlclient-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties \
        imagemagick \
        ffmpeg \
        ghostscript \
        phantomjs \
        pngcrush \
        libturbojpeg \
        ruby2.2 ruby2.2-dev \
        nodejs \
    && apt-get autoremove -y \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/* \

RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc && mkdir /app
WORKDIR /app

CMD ["bash"]

