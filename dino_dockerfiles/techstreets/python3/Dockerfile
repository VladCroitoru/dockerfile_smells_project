FROM python:3.6
MAINTAINER bradojevic@gmail.com

RUN apt-get update && apt-get install -y \
    gcc gettext mysql-client libmysqlclient-dev \
    postgresql-client libpq-dev sqlite3 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install mysqlclient psycopg2

ENV APP_ROOT /opt/app

# Define working directory.
RUN mkdir -p ${APP_ROOT}
# install common tools
RUN apt-get update && apt-get install -y net-tools curl wget vim git
RUN pip install --upgrade pip

WORKDIR ${APP_ROOT}
VOLUME ['${APP_ROOT}']

EXPOSE 80 443 8080 8000

CMD ["tail", "-f", "/dev/null"]
