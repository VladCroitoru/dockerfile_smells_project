FROM debian
MAINTAINER David Personette <dperson@gmail.com>

RUN export DEBIAN_FRONTEND='noninteractive' && \
    export url='https://download.owncloud.org/community' && \
    export version='10.4.1' && \
    export sha256sum='63f32048225c6bc4534c6757e8beee65fc845a35126899e85d78' && \
    apt-get update -qq && \
    apt-get install -qqy --no-install-recommends bzip2 ca-certificates curl \
                openssl smbclient php7.3-bz2 php7.3-curl php7.3-fpm php7.3-gd \
                php7.3-gmp php7.3-imap php7.3-intl php7.3-json php7.3-ldap \
                php7.3-mbstring php7.3-mysql php7.3-opcache php7.3-pgsql \
                php7.3-sqlite3 php7.3-xml php7.3-zip php7.3-apcu-bc \
                php7.3-imagick php7.3-memcached php7.3-redis procps \
                $(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}') &&\
    file="owncloud-${version}.tar.bz2" && \
    echo "downloading $file ..." && \
    curl -LOSs https://github.com/dperson/owncloud/raw/master/nginx.conf && \
    curl -LOSs ${url}/$file && \
    sha256sum $file | grep -q "$sha256sum" || \
    { echo "expected $sha256sum, got $(sha256sum $file)"; exit 13; } && \
    file=/etc/php/7.3/fpm/php-fpm.conf && \
    sed -i 's|^;*\(daemonize\) *=.*|\1 = no|' $file && \
    sed -i 's|^;*\(error_log\) *=.*|\1 = /proc/self/fd/2|' $file && \
    file=/etc/php/7.3/fpm/pool.d/www.conf && \
    sed -i 's|^;*\(access_log\) *=.*|\1 = /proc/self/fd/2|' $file && \
    sed -i 's|^;*\(/catch_workers_output *=.*\)|\1|' $file && \
    sed -i 's|^;*\(chdir\) *=.*|\1 = /srv/www|' $file && \
    sed -i 's|^;*\(/clear_env *=.*\)|\1|' $file && \
    sed -i 's|^;*\(listen\) *=.*|\1 = [::]:9000|' $file && \
    unset file && \
    for i in /etc/php/7.3/*/php.ini; do \
        sed -i 's|^;*\(doc_root\) *=.*|\1 = "/srv/www"|' $i; \
        sed -i '/php_errors/s|^;*\(error_log\) *=.*|\1 = /proc/self/fd/2|' $i; \
        sed -i 's|^;*\(expose_php\) *=.*|\1 = On|' $i; \
        sed -i 's|^;*\(max_execution_time\) *=.*|\1 = 3600|' $i; \
        sed -i 's|^;*\(max_input_time\) *=.*|\1 = 3600|' $i; \
        sed -i 's|^;*\(opcache.enable\) *=.*|\1 = 1|' $i; \
        sed -i 's|^;*\(opcache.enable_cli\) *=.*|\1 = 1|' $i; \
        sed -i 's|^;*\(opcache.fast_shutdown\) *=.*|\1 = 1|' $i; \
        sed -i 's|^;*\(opcache.interned_strings_buffer\) *=.*|\1 = 8|' $i; \
        sed -i 's|^;*\(opcache.max_accelerated_files\) *=.*|\1 = 4000|' $i; \
        sed -i 's|^;*\(opcache.memory_consumption\) *=.*|\1 = 128|' $i; \
        sed -i 's|^;*\(opcache.revalidate_freq\) *=.*|\1 = 60|' $i; \
        sed -i 's|^;*\(output_buffering\) *=.*|\1 = 0|' $i; \
        sed -i 's|^;*\(post_max_size\) *=.*|\1 = 16G|' $i; \
        sed -i 's|^;*\(upload_max_filesize\) *=.*|\1 = 16G|' $i; \
    done && \
    echo '\n[apc]\napc.enable_cli = 1' >>/etc/php/7.3/mods-available/apcu.ini&&\
    apt-get purge -qqy ca-certificates curl && \
    apt-get autoremove -qqy && apt-get clean && \
    ln -s /srv/www /var/ && \
    mkdir -p /run/php && \
    rm -rf /var/lib/apt/lists/* /tmp/* $file
COPY owncloud.sh /usr/bin/

VOLUME ["/srv/www/owncloud"]

EXPOSE 9000

ENTRYPOINT ["owncloud.sh"]