FROM 659153740712.dkr.ecr.us-east-1.amazonaws.com/zappi/base/zappi-api-docs:1.0.0

# ARGs & ENVs
ARG APP_USER="app"
ENV HOME="/home/${APP_USER}" \
    BUNDLE_PATH="/srv/bundle"
ARG CODE_PATH="/srv/code"

# User
RUN groupadd -g 9999 ${APP_USER} && \
    useradd --system --create-home -u 9999 -g 9999 ${APP_USER} && \
    mkdir -p ${BUNDLE_PATH} ${CODE_PATH}

WORKDIR ${CODE_PATH}

# Cache, install & clean ruby gem dependencies
COPY Gemfile Gemfile.lock ./
RUN export BUNDLER_VERSION=$(cat Gemfile.lock | tail -1 | tr -d "[:space:]") && \
    gem install bundler -v "${BUNDLER_VERSION}" && \
    bundle config set frozen 'true' && \
    bundle config set without "test development" && \
    bundle install --jobs 8 --retry 3 && \
    rm -rf ${BUNDLE_PATH}/{cache,ruby/*/cache}

ADD . ${CODE_PATH}

# Generate static files from raw docs
RUN bundle exec middleman build

# Fix permission issue - Nginx
RUN touch /var/run/nginx.pid && \
    chown -R ${APP_USER}:${APP_USER} /var/run/nginx.pid && \
    chown -R ${APP_USER}:${APP_USER} /var/cache/nginx && \
    chown -R ${APP_USER}:${APP_USER} /var/log/nginx && \
    chown -R ${APP_USER}:${APP_USER} /etc/nginx/conf.d

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

ARG GIT_RELEASE
ENV GIT_RELEASE="${GIT_RELEASE:-unset}"

# Gracefully shutdown nginx
STOPSIGNAL SIGQUIT

# Run as app
USER ${APP_USER}:${APP_USER}
