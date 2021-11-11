# vim:set ft=dockerfile:
FROM postgres:latest

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["postgres"]
