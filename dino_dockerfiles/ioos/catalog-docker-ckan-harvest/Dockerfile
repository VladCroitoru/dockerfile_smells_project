FROM ioos/catalog-docker-base

COPY ./contrib/my_init.d /etc/my_init.d

CMD ["/sbin/my_init", "--", "/bin/services/harvester/run"]

