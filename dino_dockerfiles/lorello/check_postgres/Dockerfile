FROM postgres:latest

ADD https://raw.githubusercontent.com/bucardo/check_postgres/master/check_postgres.pl /usr/local/bin/check_postgres

RUN chmod +x /usr/local/bin/check_postgres

ENTRYPOINT [ "/usr/local/bin/check_postgres" ]

CMD [ "--help" ]
