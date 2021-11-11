FROM python:3.8.1-buster

ENV PYTHONUNBUFFERED 1

# provide dummy values for required env variables
ENV CWWED_ARCHIVES_ACCESS_KEY_ID ''
ENV CWWED_ARCHIVES_SECRET_ACCESS_KEY ''
ENV SLACK_BOT_TOKEN ''

# include app
RUN mkdir /app
ADD . /app
ADD docker-entrypoint.sh /app
WORKDIR /app

RUN echo "Installing dependencies and building application" \
    && wget -qO- https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get update && apt-get install -y \
        libgdal-dev \
        gdal-bin \
        nodejs \
        python3-tk \
        libudunits2-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && npm --prefix frontend install \
    && npm --prefix frontend run build-prod \
    && mkdir -p staticfiles && python manage.py collectstatic --no-input \
    && apt-get remove -y \
        libgdal-dev \
        nodejs \
    && apt-get autoremove -y \
    && rm -rf frontend/node_modules \
    && rm -rf /var/lib/apt/lists/* \
    && true

EXPOSE 80

VOLUME /media/bucket/cwwed

ENTRYPOINT ["/app/docker-entrypoint.sh"]
