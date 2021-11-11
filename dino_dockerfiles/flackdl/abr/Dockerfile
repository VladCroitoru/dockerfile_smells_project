FROM ubuntu:18.04

# add app
ADD . /app/
WORKDIR /app

# update and install dependencies
RUN apt-get update && \
    apt-get install -y \
        curl && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y \
        nodejs \
        git \
        python3-pip \
        python3-dev \
        python3-setuptools \
        python3-cairo \
        build-essential \
        libpq-dev \
        libffi-dev \
        libxml2-dev \
        libxslt1-dev \
        libz-dev \
        libpango1.0-0 \
    && true && \
    # install and build angular app
    npm --prefix ng install --silent && \
    mkdir -p ng-assets && \
    npm --prefix ng run build && \
    # install python dependencies
    pip3 install -r requirements.txt && \
    # remove things
    apt-get remove -y \
        git \
        nodejs \
        curl \
    && true && \
    apt-get autoremove -y && \
    rm -rf ng/node_modules && \
    true

CMD \
    # build/migrate tables
    python3 manage.py migrate && \
    # run init
    python3 manage.py init && \
    # collect django static files
    python3 manage.py collectstatic --noinput && \
    # start web server
    gunicorn -w 3 --timeout 20 -b :${PORT:-80} abr.wsgi
