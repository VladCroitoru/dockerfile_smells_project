FROM python:2.7

COPY docker/newrelic_agent /usr/local/bin/agent

RUN pip install https://github.com/relaxart/newrelic-plugin-agent/archive/master.zip \
    && pip install Jinja2 \
    && pip install psycopg2 \
    && chmod +x /usr/local/bin/agent/run.sh

WORKDIR /usr/local/bin/agent

CMD ["/usr/local/bin/agent/run.sh"]