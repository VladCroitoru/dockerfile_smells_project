FROM nuocw/buildpack-deps:centos7
MAINTAINER "TOIDA Yuto" <toida.yuto@b.mbox.nagoya-u.ac.jp>

# dependencies for building php
RUN yum update -y && yum install -y epel-release && yum clean all
RUN yum update -y && yum install -y \
    bison \
    libmcrypt-devel \
    libtidy-devel \
    re2-devel \
    libicu-devel \
    && yum clean all

## add user "nuocw"
#RUN useradd nuocw
#USER nuocw
#ENV HOME="/home/nuocw"
ENV HOME="/root"
WORKDIR ${HOME}

# install anyenv
RUN git clone https://github.com/riywo/anyenv .anyenv
ENV ANYENV_ROOT="${HOME}/.anyenv"
ENV ANYENV_ENV="${ANYENV_ROOT}/envs"
RUN echo 'export PATH="${ANYENV_ROOT}/bin:${PATH}"' >> .bash_profile
RUN echo 'eval "$(anyenv init -)"' >> .bash_profile

# update anyenv
RUN mkdir -p .anyenv/plugins
RUN git clone https://github.com/znz/anyenv-update.git ${ANYENV_ROOT}/plugins/anyenv-update
# RUN git clone https://github.com/ngyuki/phpenv-composer.git ${ANYENV_ROOT}/plugins/anyenv-composer

ENV PATH="${HOME}/.anyenv/bin:${PATH}"
RUN eval "$(anyenv init -)"

# phpenv
RUN anyenv install phpenv
ENV PHPENV_ROOT=${ANYENV_ENV}/phpenv
ENV PATH="${PHPENV_ROOT}/bin:${PHPENV_ROOT}/shims:${PATH}"
# RUN git clone https://github.com/ngyuki/phpenv-composer.git ${PHPENV_ROOT}/plugins/phpenv-composer
RUN eval "$(anyenv init -)"

# PHP5.4 is End of Life
#RUN PHP_54_LATEST=$(phpenv install -l | grep -P "5\.4\.[0-9]+" | sed -e s/^\\s*// | tail -n1) && phpenv install $PHP_54_LATEST && phpenv rehash
# PHP5.5 is End of Life
#RUN PHP_55_LATEST=$(phpenv install -l | grep -P "5\.5\.[0-9]+" | sed -e s/^\\s*// | tail -n1) && phpenv install $PHP_55_LATEST && phpenv rehash
RUN PHP_56_LATEST=$(phpenv install -l | grep -P "5\.6\.[0-9]+" | sed -e s/^\\s*// | tail -n1) && phpenv install $PHP_56_LATEST && phpenv rehash
RUN PHP_70_LATEST=$(phpenv install -l | grep -P "7\.0\.[0-9]+" | sed -e s/^\\s*// | tail -n1) && phpenv install $PHP_70_LATEST && phpenv rehash
RUN PHP_71_LATEST=$(phpenv install -l | grep -P "7\.1\.[0-9]+" | sed -e s/^\\s*// | tail -n1) && phpenv install $PHP_71_LATEST && phpenv rehash
RUN PHP_72_LATEST=$(phpenv install -l | grep -P "7\.2\.[0-9]+" | sed -e s/^\\s*// | tail -n1) && phpenv install $PHP_72_LATEST && phpenv rehash && phpenv global $PHP_72_LATEST

RUN mkdir ${HOME}/bin && curl -sS https://getcomposer.org/installer | php -- --install-dir=${HOME}/bin --filename=composer
RUN echo 'export PATH=${HOME}/bin:${PATH}' >> .bash_profile
ENV PATH=${HOME}/bin:${PATH}
RUN rm -rf /tmp/php-build

RUN find ~/ -type f -name "php.ini" -exec sed -i '/;date.timezone/c\date.timezone = "Asia/Tokyo"' {} \;
RUN composer global require hirak/prestissimo

CMD ["/bin/bash", "-c"]
