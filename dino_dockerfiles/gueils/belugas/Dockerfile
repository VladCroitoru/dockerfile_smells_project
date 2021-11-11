# 1: Use ruby 2.3.3 as base:
FROM ruby:2.3.3-alpine

# 2: We'll set the application path as the working directory
WORKDIR /usr/src/app

# 3: We'll add the app's binaries path to $PATH, and set the environment name to 'production':
ENV HOME=/usr/src/app PATH=/usr/src/app/bin:$PATH BELUGAS_DOCKER=true

VOLUME /code

# 4: Install the particular runtime dependencies, including the Docker client.
# NOTE: To run belugas, we need to install the Docker client, so we can launch sibling containers
# runing the belugas cli stuff. For this to happen, the docker service socket must be mounted inside
# the app container.
#
# Read https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/ for more details.
#
# Install commands based on https://hub.docker.com/_/docker Dockerfiles:

# 4.1: Install Docker client:
RUN set -ex \
  && apk add --no-cache --virtual .app-builddeps curl \
  && export DOCKER_BUCKET=get.docker.com \
  && export DOCKER_VERSION=1.12.5 \
  && export DOCKER_SHA256=0058867ac46a1eba283e2441b1bb5455df846144f9d9ba079e97655399d4a2c6 \
  && curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
  && apk del .app-builddeps

# 4.2: Copy just the Gemfile & Gemfile.lock, to avoid the build cache failing whenever any other
# file changed and installing dependencies all over again - a must if your'e developing this
# Dockerfile...
ADD ./Gemfile* /usr/src/app/

# 4.3: Install build + runtime dependencies, install/build the app gems, and remove build deps:
RUN set -ex \
  && apk add --no-cache --virtual .app-builddeps build-base \
  && bundle install --without development test \
  && apk del .app-builddeps

# 5: Copy the rest of the application code, then change the owner of the code to 'app':
ADD . /usr/src/app

# 6: Set '/code' as the default working directory:
WORKDIR /code

# 7: Set the belugas executable script as the sole entrypoint for this container:
ENTRYPOINT ["/usr/src/app/bin/belugas"]
