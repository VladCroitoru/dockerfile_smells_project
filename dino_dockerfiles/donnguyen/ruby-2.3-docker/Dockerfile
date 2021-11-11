FROM ubuntu:trusty

RUN apt-get update && \
    apt-get install -qy software-properties-common && \
    apt-get install -qy libgs-dev && \
    apt-get install -qy ghostscript && \
    apt-get install -qy imagemagick --fix-missing && \
    apt-get install -qy libc6 libstdc++6 zlib1g libpng12-0 libjpeg-turbo8 \
                        libssl1.0.0 libfreetype6 libicu52 fontconfig \
                        libx11-6 libxext6 libxrender1 libxcb1 xfonts-base xfonts-75dpi wget git

RUN apt-add-repository -y ppa:brightbox/ruby-ng
RUN add-apt-repository ppa:ecometrica/servers

RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN wget --quiet -O - https://deb.nodesource.com/setup_9.x | sudo -E bash -
RUN wget --quiet -O - https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get upgrade -y

# Ruby and dependencies
RUN apt-get install -qy curl nodejs libpq-dev postgresql-9.5 postgresql-contrib-9.5 build-essential \
                        ruby2.3 ruby2.3-dev yarn

RUN gem install bundler --no-ri --no-rdoc

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*