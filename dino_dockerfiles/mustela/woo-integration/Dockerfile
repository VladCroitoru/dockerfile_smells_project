############################################################
# PLEASE, DO NOT USE THIS IMAGE FOR ANYTHING THAN PLAYING
############################################################
FROM conetix/wordpress-with-wp-cli
MAINTAINER Emiliano Jankowski

COPY woo_integration.zip /scripts/plugins/
COPY do_magic.sh /scripts/
RUN chmod +x /scripts/do_magic.sh

CMD ["/scripts/do_magic.sh"]
