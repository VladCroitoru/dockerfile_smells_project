
# Pull base image.
FROM ubuntu:16.04
RUN dpkg --add-architecture i386
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt update && apt upgrade -y
RUN apt install -y curl build-essential git openssh-client wget software-properties-common python-software-properties apt-transport-https icnsutils graphicsmagick mono-runtime  mono-complete  libmono-system-core4.0-cil mapnik-utils libmapnik-dev python-pip
RUN wget -nc https://dl.winehq.org/wine-builds/Release.key && apt-key add Release.key && apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ && apt update
RUN apt-get install -y --install-recommends winehq-stable
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt install -y nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt update && apt install yarn
RUN pip install awscli
RUN curl -O https://github.com/neteoc/neteoc-desktop/blob/master/package.json
RUN yarn install
