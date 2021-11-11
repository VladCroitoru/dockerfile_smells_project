FROM alpin3/php-apache:3.4
MAINTAINER kost - https://github.com/kost

RUN apk --update --no-cache add wget ca-certificates \
    && mkdir /php \
    && cd /php \
    && wget -O hop.php https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/php/hop.php \
    && echo "Success"

ADD scripts/ /scripts
