################################################################################
#                                                                              #
#                                 {o,o}                                        #
#                                 |)__)                                        #
#                                 -"-"-                                        #
#                                                                              #
################################################################################

#################################---INFO---#####################################

FROM kendu/php:5.6
MAINTAINER devops@kendu.si

################################################################################

################################---BUILD---#####################################

RUN apt-get update; \
    apt-get install -q -y \
        git \
        curl \
        wget \
        build-essential \
        make \
        npm \
        ruby-full

RUN ln -s /usr/bin/nodejs /usr/bin/node; \
    curl -sL https://deb.nodesource.com/setup_5.x | bash -; \
    apt-get install -y -q         nodejs; \
    npm install -g npm
RUN npm install -g \
    bower \
    grunt \
    grunt-cli \
    gulp \
    load-grunt-tasks \
    time-grunt \
    webpack \
    raml2html; \
apt-get clean

RUN gem install compass
RUN phpenmod php5-mcrypt

RUN curl -sS https://getcomposer.org/installer | php && \
mv composer.phar /usr/local/bin/composer


################################################################################
