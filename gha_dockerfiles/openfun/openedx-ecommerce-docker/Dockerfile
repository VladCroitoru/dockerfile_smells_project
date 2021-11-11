# OpenEdx ECommerce

ARG DOCKER_UID=1000
ARG DOCKER_GID=1000

# E-Commerce release archive url to build our image with
ARG EDXEC_ARCHIVE_URL=https://github.com/edx/ecommerce/archive/master.tar.gz

# ---- Base image to inherit from ----
FROM python:2.7-stretch as base


# ---- Release Download ----
FROM base as downloads

WORKDIR /downloads

# Install curl
RUN apt-get update && \
    apt-get install -y curl

# Download ecommerce release
ARG EDXEC_ARCHIVE_URL
RUN curl -sLo ecommerce.tgz ${EDXEC_ARCHIVE_URL} && \
    mkdir /downloads/ecommerce && \
    tar xzf ecommerce.tgz -C /downloads/ecommerce --strip-components=1

# ---- Front-end builder image ----
FROM node:10 as front-builder

USER node:node
WORKDIR /home/node

# Install node dependencies
COPY --from=downloads /downloads/ecommerce/package.json ./
RUN npm install

# Copy front-end sources
COPY --from=downloads --chown=node:node /downloads/ecommerce/ecommerce/static ./ecommerce/static

# Install bower dependencies
#
# Note that this should be done after copying front-end sources as the build
# target path is the "ecommerce/static" directory
COPY --from=downloads /downloads/ecommerce/bower.json /downloads/ecommerce/.bowerrc ./
RUN $(npm bin)/bower install

# Build the front-end
COPY --from=downloads /downloads/ecommerce/build.js .
RUN $(npm bin)/r.js -o build.js


# ---- Back-end builder image ----
FROM base as back-builder

WORKDIR /builder

# Add installation directory to the PYTHONPATH to allow .pth file support
# (this is required to install some dependencies)
ENV PYTHONPATH /install/lib/python2.7/site-packages

# Install python dependencies
COPY --from=downloads /downloads/ecommerce/requirements ./
RUN mkdir -p /install/src && \
    pip install --prefix=/install --src=/install/src -r production.txt


# ---- Core application image ----
FROM base as core

WORKDIR /app

# Install gettext
RUN apt-get update && \
    apt-get install -y \
      gettext && \
    rm -rf /var/lib/apt/lists/*

# Copy installed python dependencies
COPY --from=back-builder /install /usr/local
# Editable packages available via egg-links point to /install/src
RUN ln -s /usr/local /install

# Copy runtime-required files
COPY --from=downloads /downloads/ecommerce /app

# Copy front-end build
COPY --from=front-builder /home/node/ecommerce/static /app/ecommerce/static

# Compile styles
#
# Note that the ECOMMERCE_CFG environment variable should be defined and point
# to an existing YAML formatted file while using production settings. But. The
# LOGGING setting uses a syslog handler that cannot work as is in a Docker
# container, so we should override it in our ECOMMERCE_CFG file.
COPY ./docker/files/usr/local/etc/ecommerce /usr/local/etc/ecommerce
ENV ECOMMERCE_CFG /usr/local/etc/ecommerce/local.yaml
# The update_assets management command is not implemented in old releases, we
# ignore its call failure for backward-compatibility as assets have already
# been build in a previous stage in this case.
RUN python manage.py update_assets --skip-collect --settings=ecommerce.settings.production || \
      echo "Assets update failed and will be ignored (old release)"

# Copy default entrypoint script
COPY ./docker/files/usr/local/bin/entrypoint /usr/local/bin/entrypoint

# Gunicorn
RUN mkdir -p /usr/local/etc/gunicorn
COPY docker/files/usr/local/etc/gunicorn/edxec.py /usr/local/etc/gunicorn/edxec.py

# Give the "root" group the same permissions as the "root" user on /etc/passwd
# to allow a user belonging to the root group to add new users; typically the
# docker user (see entrypoint).
RUN chmod g=u /etc/passwd

# Un-privileged user running the application
ARG DOCKER_UID
ARG DOCKER_GID
USER ${DOCKER_UID}:${DOCKER_GID}

# We wrap commands run in this container by the following entrypoint that
# creates a user on-the-fly with the container user ID (see USER) and root group
# ID.
ENTRYPOINT [ "/usr/local/bin/entrypoint" ]


# ---- Production image ----
FROM core as production

WORKDIR /app

# Default settings
# Note that the ECOMMERCE_CFG environment variable is defined in the core stage
ENV DJANGO_SETTINGS_MODULE ecommerce.settings.production

# The default command runs gunicorn WSGI server
CMD gunicorn -c /usr/local/etc/gunicorn/edxec.py ecommerce.wsgi:application
