FROM debian:8

RUN apt-get update && \
    apt-get install --no-install-recommends --yes libdbi-perl libdbd-mysql-perl spamassassin pyzor && \
    apt-get autoclean && apt-get --yes autoremove && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV BAYES_ADDRESS=BayesDatabase \
    BAYES_USER=bayes \
    BAYES_PASSWORD=bayes \
    ALLOWED_IP_RANGES=0.0.0.0/0 \
    MIN_CHILDREN=1 \
    MAX_CHILDREN=5 \
    MIN_SPARE=1 \
    MAX_SPARE=2

RUN mkdir -p /nonexistent/.pyzor/ && chown -R nobody:nogroup /nonexistent

COPY [ "entrypoint.sh", "/" ]

EXPOSE 783

ENTRYPOINT [ "/entrypoint.sh" ]
