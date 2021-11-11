# Pull from an alpine with runit already pre-enabled
FROM nimmis/alpine-micro:3.7

# Copying just our requirements
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Pre-install APK stuff, then run pip install, and clean up our virtual packages
RUN apk update                                                            && \
    apk add --no-cache postgresql-dev python                              && \
    apk add --no-cache --virtual .build-deps build-base py-pip python-dev && \
    pip install --no-cache-dir -r requirements.txt                        && \
    apk del .build-deps                                                   && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

# Copy our app and enable it.  Once built once, this should be the only thing that changes 
#   (provided that the requirements.txt doesn't change, that will make above re-run)
COPY . /app
RUN mkdir -p /etc/service/pgsqlstatsd                                     && \
    mv /app/pgsqlstatsd.service /etc/service/pgsqlstatsd/run              && \
    chmod +x /etc/service/pgsqlstatsd/run
