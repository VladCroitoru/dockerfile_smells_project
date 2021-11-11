FROM debian:8.7

LABEL maintainer "j.zelger@techdivision.com"

# copy all filesystem relevant files
COPY fs /tmp/

# start install routine
RUN \
    # install base tools
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-recommends \
        vim tar wget curl apt-transport-https ca-certificates net-tools htop python-pip pv && \

    # copy repository files
    cp -r /tmp/etc/apt /etc && \

    # add repository keys
    curl https://www.dotdeb.org/dotdeb.gpg | apt-key add - && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \

    # update repositories
    apt-get update && \

    # install ...
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-recommends \
        # general tools
        ssh openssl rsync git graphicsmagick nodejs build-essential rubygems ruby-dev ruby-compass \
        #  php 7.0
        php7.0 php7.0-cli php7.0-common php7.0-curl php7.0-gd php7.0-mcrypt php7.0-mysql php7.0-soap \
        php7.0-json php7.0-zip php7.0-intl php7.0-bcmath php7.0-xsl php7.0-xml php7.0-mbstring php7.0-xdebug \
        php7.0-mongodb php7.0-ldap php7.0-imagick php7.0-readline && \

    # install current compass and sass via gem
    gem update —system && \
    gem install compass sass && \

    # install gulp
    npm install -g gulp-cli && \

    # install composer
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    composer global require hirak/prestissimo && \

    # prepare build folder
    mkdir /build && \

    # cleanup
    apt-get clean && \
    rm -rf /tmp/*

# define volumes
VOLUME ["/build"]

# define workdir
WORKDIR /build