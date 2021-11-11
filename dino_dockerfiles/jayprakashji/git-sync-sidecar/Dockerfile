FROM composer:1.3

COPY git-sync.sh /
RUN chmod +x /git-sync.sh

ENTRYPOINT ["/git-sync.sh"]