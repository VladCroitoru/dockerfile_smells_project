FROM python:3.6-stretch

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        mysql-client \
        postgresql-client-10 \
    && rm -rf /var/lib/apt/lists/*

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 \
    && echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/3.6 main" > /etc/apt/sources.list.d/mongodb-org-3.6.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        mongodb-org-tools \
    && rm -rf /var/lib/apt/lists/*

RUN wget "https://downloads.rclone.org/rclone-current-linux-amd64.deb" \
    && dpkg -i ./rclone-current-linux-amd64.deb \
    && rm ./rclone-current-linux-amd64.deb

COPY bin/ /app

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
CMD [ "/app/entrypoint.sh" ]
