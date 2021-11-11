FROM ubuntu

ENV TZ=Europe/Amsterdam

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
    apt upgrade -y && \
    apt install software-properties-common -y && \
    apt update

RUN LC_ALL=C.UTF-8 && \
    add-apt-repository ppa:ondrej/php && \
    apt update && \
    apt install php7.4 php7.4-cli php7.4-common php7.4-xml -y && \
    php -v

RUN apt install git -y

RUN git clone https://github.com/ammartins/bankcree-5.git /srv/bankcree-5

RUN apt install wget php7.4-cli php7.4-zip unzip -y
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    HASH="$(wget -q -O - https://composer.github.io/installer.sig)"  && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN apt autoclean -y && \
    apt autoremove -y

#RUN tail -f /dev/null
