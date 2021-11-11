FROM clarencep/lap7:centos7

RUN DEBIAN_FRONTEND="noninteractive" \
    && yum install -y zip php71w-pear php71w-devel gcc make wget \
    && pecl install redis \
    && echo 'extension=redis.so' > /etc/php.d/redis.ini \
    && mkdir -p /usr/src/php-profiler-extension \
    && wget -O /tmp/php-profiler-extension.tar.gz https://github.com/tideways/php-profiler-extension/archive/v4.1.2.tar.gz \
    && tar -xzf /tmp/php-profiler-extension.tar.gz -C /usr/src/php-profiler-extension --strip-components=1 \
    && cd /usr/src/php-profiler-extension && phpize  \
    && ./configure && make && make install \
    && echo 'extension=tideways.so' > /etc/php.d/tideways.ini \
    && echo 'tideways.auto_prepend_library=0' >> /etc/php.d/tideways.ini \
    && php -r '$exts = "tokenizer|mbstring|pdo_mysql|openssl|mcrypt|xml|dom|redis|tideways"; $missing = array_map(function($m){ return !extension_loaded($m) ? $m : ""; }, explode("|", $exts)); $missing = array_filter($missing); if ($missing) { echo "Error: Missing PHP extesions: " . implode(",", $missing) . "\n"; exit(1); }' \
    && /usr/sbin/httpd -t \
    && yum erase -y zip php71w-pear php71w-devel gcc make wget \
    && find /var/log -type f -print0 | xargs -0 rm -rf /tmp/* \
    && yum clean all

