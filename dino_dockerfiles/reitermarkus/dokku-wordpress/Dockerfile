FROM wordpress:cli-php7.4 as cli

FROM wordpress:5-php7.4-apache

RUN apt-get update \
 && apt-get install -y gnupg less \
 && rm -rf /var/lib/apt/lists/*

COPY --from=cli /usr/local/bin/wp /usr/local/bin/wp

RUN wp --allow-root --version

RUN sed -i '/haveConfig=$/i \\source /usr/local/bin/pre-entrypoint.sh'  "$(which docker-entrypoint.sh)"
COPY pre-entrypoint.sh /usr/local/bin/

RUN sed -i "/# now that we're definitely done/i   \\	source /usr/local/bin/entrypoint.sh\\ \n" "$(which docker-entrypoint.sh)"
COPY entrypoint.sh /usr/local/bin/

RUN rm -r /usr/src/wordpress/wp-content/themes/twenty*   \
 && rm -r /usr/src/wordpress/wp-content/plugins/akismet        \
 && rm    /usr/src/wordpress/wp-content/plugins/hello.php \
 && sed -i 's/\[ "$(ls -A)" \]/false/' "$(which docker-entrypoint.sh)"
