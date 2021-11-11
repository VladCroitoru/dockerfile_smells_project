FROM debian:bullseye-slim AS core

# Build arguments
ARG EXTRAS="ldap,s3"
ARG APP_VERSION=""

# Configure Python to be nice inside Docker and pip to stfu
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DEFAULT_TIMEOUT 100
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1
ENV PIP_EXTRA_INDEX_URL https://edugit.org/api/v4/projects/461/packages/pypi/simple
ENV PIP_USE_DEPRECATED legacy-resolver
ENV DEBIAN_FRONTEND noninteractive

# Configure app settings for build and runtime
ENV ALEKSIS_static__root /usr/share/aleksis/static
ENV ALEKSIS_media__root /var/lib/aleksis/media
ENV ALEKSIS_backup__location /var/lib/aleksis/backups
ENV ALEKSIS_dev__uwsgi__celery false

# Install necessary Debian and PyPI packages for build and runtime
RUN apt-get -y update && \
    apt-get -y install eatmydata && \
    eatmydata apt-get -y upgrade && \
    eatmydata apt-get install -y --no-install-recommends \
        build-essential \
        chromium \
	dumb-init \
	gettext \
	libpq5 \
	libpq-dev \
	libssl-dev \
	postgresql-client \
	python3-dev \
	python3-magic \
	python3-pip \
	uwsgi \
	uwsgi-plugin-python3 \
	yarnpkg

# Install extra dependencies
RUN   case ",$EXTRAS," in \
        (*",ldap,"*) \
          eatmydata apt-get install -y --no-install-recommends \
            libldap2-dev \
            libsasl2-dev \
            ldap-utils \
	  ;; \
      esac

# Install core
RUN set -e; \
    mkdir -p ${ALEKSIS_static__root} \
             ${ALEKSIS_media__root} \
             ${ALEKSIS_backup__location}; \
    eatmydata pip install AlekSIS-Core\[$EXTRAS\]$APP_VERSION

# Define entrypoint, volumes and uWSGI running on port 8000
EXPOSE 8000
VOLUME ${ALEKSIS_media__root} ${ALEKSIS_backup__location}
COPY docker-startup.sh /usr/local/bin/aleksis-docker-startup
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/usr/local/bin/aleksis-docker-startup"]

# Install assets
FROM core as assets
RUN eatmydata aleksis-admin yarn install; \
    eatmydata aleksis-admin collectstatic --no-input; \
    rm -rf /usr/local/share/.cache

# Clean up build dependencies
FROM assets AS clean
RUN set -e; \
    eatmydata apt-get remove --purge -y \
        build-essential \
        gettext \
        libpq-dev \
        libssl-dev \
        libldap2-dev \
        libsasl2-dev \
        python3-dev; \
    eatmydata apt-get autoremove --purge -y; \
    apt-get clean -y; \
    rm -rf /root/.cache

# Drop privileges for runtime to www-data
FROM clean AS unprivileged
WORKDIR /var/lib/aleksis
RUN chown -R www-data:www-data \
     ${ALEKSIS_media__root} \
     ${ALEKSIS_backup__location}
USER 33:33

# Additional steps
ONBUILD ARG APPS
ONBUILD ARG BUILD_DEPS
ONBUILD ARG SYSTEM_DEPS
ONBUILD USER 0:0
ONBUILD RUN set -e; \
            if [ -n "$BUILD_DEPS" ]; then \
                eatmydata apt-get update; \
                eatmydata apt-get install -y $BUILD_DEPS; \
            fi; \
            if [ -n "$SYSTEM_DEPS" ]; then \
                eatmydata apt-get update; \
                eatmydata apt-get install -y $SYSTEM_DEPS; \
            fi;
ONBUILD RUN set -e; \
            if [ -n "$APPS" ]; then \
                eatmydata pip install $APPS; \
            fi; \
            eatmydata aleksis-admin yarn install; \
            eatmydata aleksis-admin collectstatic --no-input; \
            rm -rf /usr/local/share/.cache; \
            eatmydata apt-get remove --purge -y yarnpkg $BUILD_DEPS; \
            eatmydata apt-get autoremove --purge -y; \
            apt-get clean -y; \
            rm -f /var/lib/apt/lists/*_*; \
            rm -rf /root/.cache
ONBUILD USER 33:33
