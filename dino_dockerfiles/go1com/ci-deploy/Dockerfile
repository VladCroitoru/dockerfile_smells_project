FROM ubuntu:xenial

RUN apt-get update -qq && apt-get install -yqq \
        apt-transport-https \
        autoconf \
        ca-certificates \
        curl \
        language-pack-en-base \
        lxc \
        software-properties-common \
    && set -x \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" \
    && LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php \
    && apt-get update \
    && apt-get install docker-ce -yqq \
    && curl -s -L https://github.com/docker/compose/releases/latest | \
        egrep -o '/docker/compose/releases/download/[0-9.]*/docker-compose-Linux-x86_64' | \
        wget --base=http://github.com/ -i - -O /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && /usr/local/bin/docker-compose --version \
    && curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod +x kubectl && mv kubectl /usr/local/bin/kubectl \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get update -qq  \
    && apt-get install -qqy php7.1-cli php7.1-mbstring php7.1-soap php7.1-curl php7.1-mongodb php7.1-gd php7.1-mcrypt php7.1-bcmath php7.1-mysql php7.1-sqlite3 php7.1-xml libmcrypt-dev libicu-dev libxml2-dev libssl-dev libffi-dev curl git-core unzip python2.7 jq g++ python-software-properties libfontconfig build-essential ruby-dev nodejs gettext default-jre default-jdk \
    && apt-get clean -qqy \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require go1/deploy-helper:* \
    && ln -s ~/.composer/vendor/bin/deploy-helper /usr/local/bin/deploy-helper \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && pip install awscli s3cmd \
    && gem install --no-rdoc --no-ri compass foundation sass \
    && curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-v0.6.6 \
    && chmod +x /usr/local/bin/ecs-cli \
    && bash -c 'npm config set -g progress false' \
    && bash -c 'npm install -g bower yarn @angular/cli grunt-cli gulp-cli jira-cmd phantomjs-prebuilt utf-8-validate optipng jpegtran pngquant gifsicle bufferutil jshint ycssmin recess imagemin imagemin-gifsicle imagemin-jpegtran imagemin-optipng imagemin-pngquant optipng-bin jpegtran-bin newman nightmare mocha serverless serverless-webpack webpack typescript uglify-js' \
    && bash -c 'yarn global add npm --silent' \
    && mkdir -p ~/.ssh \
    && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
