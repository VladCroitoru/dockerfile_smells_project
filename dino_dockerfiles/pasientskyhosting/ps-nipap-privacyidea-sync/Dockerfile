FROM python:2.7

RUN apt-get update \
    && apt-get install -y -q --no-install-recommends --no-install-suggests \
        net-tools \
        tzdata \
        cron \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pynipap

# Add tini
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

COPY sync.py /sync.py
COPY run.sh /run.sh
COPY crontab /etc/cron.d/nipap-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/nipap-cron

ENTRYPOINT ["/tini", "--"]
CMD ["/run.sh"]
