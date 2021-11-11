FROM ubuntu:14.04

ENV NETDISCO_DB_PASS "netdiscopass"
ENV NETDISCO_DOMAIN ""
ENV NETDISCO_RO_COMMUNITY "public"
ENV NETDISCO_WR_COMMUNITY ""

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    libdbd-pg-perl \
    libsnmp-perl \
    build-essential \
    postgresql-client \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV NETDISCO_HOME "/netdisco"
RUN mkdir $NETDISCO_HOME
WORKDIR $NETDISCO_HOME

RUN curl -k -L http://cpanmin.us/ | perl - --notest --local-lib $NETDISCO_HOME/perl5 App::Netdisco
ENV PATH $NETDISCO_HOME/perl5/bin:$PATH

ADD netdisco-entry.sh /
EXPOSE 5000
ENTRYPOINT ["/netdisco-entry.sh"]
