FROM perl:latest
RUN cpan App::Sqitch && \
    cpan DBD::Pg && \
    apt-get update && \
    apt-get install postgresql-client-common postgresql-client -y --no-install-recommends && \
    apt-get clean
VOLUME [/src]
WORKDIR /src
CMD ["sqitch"]