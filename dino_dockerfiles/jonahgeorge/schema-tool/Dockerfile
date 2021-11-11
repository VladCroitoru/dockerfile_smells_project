FROM ubuntu:18.04

ENV DB_TYPE            ""
ENV DB_HOST            ""
ENV DB_PORT            ""
ENV DB_PASSWORD        ""
ENV DB_USERNAME        ""
ENV REVISION_DB_NAME   "revision"
ENV HISTORY_TABLE_NAME "history"
ENV STATIC_ALTER_DIR   ""
ENV PRE_COMMIT_HOOK    ""

RUN apt-get update && \
    apt-get install -y \
        python \
	gettext \
	wait-for-it \
        mysql-client \
	python-psycopg2 \
	python-vertica

WORKDIR /schema-tool
COPY . .

WORKDIR /schemas
ENTRYPOINT ["/schema-tool/entrypoint.sh"]
CMD ["--help"]
