FROM endika/base

MAINTAINER me@endikaiglesias.com

RUN aptitude install -y postgresql-9.3
WORKDIR /tmp
VOLUME ["/var/log/postgresql", \
        "/var/log/supervisor", \
        "/etc/postgresql/9.3/main", \
        "/var/lib/postgresql/9.3/main"]
CMD ["postgres"]
EXPOSE 5432
