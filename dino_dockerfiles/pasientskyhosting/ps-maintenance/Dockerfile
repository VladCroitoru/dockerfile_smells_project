FROM pasientskyhosting/ps-worker:mono4.8.1
MAINTAINER Andreas Krüger <ak@patientsky.com>

RUN composer_hash=$(wget -q -O - https://composer.github.io/installer.sig) && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '${composer_hash}') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');" && \
    apt-get update \
    && apt-get install -y -q --no-install-recommends \
    wget \
    net-tools \
    vim \
    tmux \
    tzdata \
    locales \
    localepurge \
    nano

# Install no locale
RUN sed -i 's/# nb_NO.UTF-8 UTF-8/nb_NO.UTF-8 UTF-8/' /etc/locale.gen && \
    ln -s /etc/locale.alias /usr/share/locale/locale.alias && \
    locale-gen nb_NO.UTF-8

RUN sed -i "s|USE_DPKG|#USE_DPKG|" /etc/locale.nopurge && localepurge

ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh

ENV MONO_GC_PARAMS="nursery-size=1g"

ENTRYPOINT ["/start.sh"]
