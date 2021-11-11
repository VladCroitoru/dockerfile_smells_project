FROM python:3.8-slim

ARG REQFILE=requirements-prod.txt

ENV PYTHONUNBUFFERED=1 \
    WORK_DIR=/opt/lcct \
    GRUNT_TASK=prod

#https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199
RUN mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7

RUN runDeps="curl gnupg build-essential libpoppler-cpp-dev pkg-config postgresql-client python3-dev python3-cffi libcairo2 libpango1.0-0 libpangocairo-1.0.0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libpq-dev libz-dev libjpeg-dev libfreetype6-dev git npm" \
    && apt-get update \
    && apt-get install -y --no-install-recommends $runDeps \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && rm -vrf /var/lib/apt/lists/*

RUN mkdir -p $WORK_DIR \
    && mkdir -p /media/uploadfiles \
    && mkdir -p /var/www/

COPY ./docker/entrypoint.sh /bin/

COPY requirements* package.json Gruntfile.js $WORK_DIR/
WORKDIR $WORK_DIR
RUN pip install --no-cache-dir -r $REQFILE \
    && npm install -g grunt-cli \
    && npm install

COPY . $WORK_DIR

RUN grunt $GRUNT_TASK

ENTRYPOINT ["entrypoint.sh"]
CMD ["run"]
