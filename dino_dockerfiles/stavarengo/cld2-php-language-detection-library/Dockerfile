FROM ubuntu:16.04

# Set the minimum Ubuntu environment
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install software-properties-common -y && \
    DEBIAN_FRONTEND=noninteractive locale-gen en_US.UTF-8 pt_BR.UTF-8 && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \
    DEBIAN_FRONTEND=noninteractive apt-get install language-pack-en-base -y && \
    DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php -y && \
    # Installs our dependencies
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apt-utils \
        git \
        apache2 \
        libapache2-mod-php5.6 \
        php5.6 \
        php5.6-dev

    # Compile the PHP CLD2 extension
RUN cd /root && \
    git clone https://github.com/fntlnz/cld2-php-ext.git --progress && \
    cd cld2-php-ext && \
    git checkout 71e34aa2ddf2e9ce5f91342bd20fa892642d5b71 && \
    git clone https://github.com/CLD2Owners/cld2.git libcld2 --progress && \
    cd libcld2 && \
    git checkout b56fa78a2fe44ac2851bae5bf4f4693a0644da7b && \
    cd internal && \
    ./compile_libs.sh && \
    cp libcld2.so /usr/local/lib && \
    cd ../.. && \
    phpize && \
    ./configure --with-cld2=libcld2 && \
    make -j && \
    make install && \
    DEBIAN_FRONTEND=noninteractive apt-get remove php5.6-dev -y && \
    DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
    echo -e "\nextension=cld2.so\n" | tee -a /etc/php/5.6/apache2/php.ini && \
    service apache2 restart
