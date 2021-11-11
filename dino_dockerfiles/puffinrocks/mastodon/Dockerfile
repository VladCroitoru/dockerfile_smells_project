FROM gargron/mastodon:v1.6.1

ENV VERSION 1.6.1

COPY create_admin.rb /mastodon/create_admin.rb

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
