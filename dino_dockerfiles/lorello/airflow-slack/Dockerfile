FROM jbergknoff/postgresql-client

RUN apk add --no-cache \
      bash \
      gzip \
      curl \
      ca-certificates

ADD https://raw.githubusercontent.com/course-hero/slacktee/master/slacktee.sh /usr/local/bin/slacktee

WORKDIR /tmp
RUN curl -L https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-linux.gz -o /tmp/go-cron-linux.gz && \
    gunzip /tmp/go-cron-linux.gz && \
    mv /tmp/go-cron-linux /usr/local/bin/go-cron

ADD check-airflow-sla.sh /usr/local/bin/check-airflow-sla
ADD run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/*

ENTRYPOINT [ "/usr/local/bin/run" ]

