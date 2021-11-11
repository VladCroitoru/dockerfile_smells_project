FROM ubuntu:20.04

MAINTAINER Alexander Petermann <petermann.a@gmx.net>

RUN adduser --system --home /var/lib/munin --shell /bin/false --uid 999 --group munin

RUN apt update -qq \
    && apt dist-upgrade -y \
    && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt install -y -qq --no-install-recommends \
        openssh-client \
        cron \
        munin \
        nginx \
        wget \
        s-nail \
        patch \
        spawn-fcgi \
        libcgi-fast-perl \
        rsyslog \
        curl \
        ca-certificates \
        libnet-snmp-perl \
        netbase \
        logrotate \
        tzdata \
    && apt clean && rm -rf /var/lib/apt/lists/* \
    && rm /etc/nginx/sites-enabled/default \
    && mkdir -p /var/cache/munin/www \
    && chown munin:munin /var/cache/munin/www \
    && mkdir -p /var/run/munin \
    && chown -R munin:munin /var/run/munin

VOLUME /var/lib/munin
VOLUME /var/log/munin

COPY ./munin.conf /etc/munin/munin.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./nginx-munin /etc/nginx/sites-enabled/munin
COPY ./start-munin.sh /munin
COPY ./munin-graph-logging.patch /usr/share/munin
COPY ./munin-update-logging.patch /usr/share/munin

RUN cd /usr/share/munin \
  && patch munin-graph < munin-graph-logging.patch \
  && patch munin-update < munin-update-logging.patch

COPY ./check-munin.sh /check
ENV HEALTH_HOSTINFO=
ENV HEALTH_CHECK_NODES=1
HEALTHCHECK --interval=5m --timeout=10s --retries=3 CMD /check || exit 1

EXPOSE 8080

CMD ["bash", "/munin"]
