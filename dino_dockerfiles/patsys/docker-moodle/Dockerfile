FROM patsys/apache
MAINTAINER Patrick Weber <pat.weber91@gmail.com>
COPY 25_moodle_setup.sh /etc/my_init.d/
ADD utils /utils/
RUN chmod u+x /etc/my_init.d/25_moodle_setup.sh
RUN apk update && apk upgrade && apk add sudo coreutils openssl lynx php5-dom php5-xmlreader php5-curl php5-zlib php5-gd php5-openssl php5-xmlrpc php5-soap php5-intl  php5-xml php5-json php5-ctype php5-zip php5-mysqli php5-iconv ca-certificates && rm -rf /var/cache/apk/*
RUN update-ca-certificates
RUN /utils/exist_moodle_update.sh
CMD ["/etc/start"]
