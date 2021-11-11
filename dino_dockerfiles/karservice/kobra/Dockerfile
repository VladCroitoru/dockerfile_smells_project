FROM alpine:3.7

# Kept separate to be interpreted in next step
ENV APP_ROOT=/app

# PIP_NO_CACHE_DIR=false actually means *no cache*. Wat.
ENV DJANGO_SETTINGS_MODULE=kobra.settings.production \
    GUNICORN_CONFIG=${APP_ROOT}/gunicorn-conf.py \
    PATH=${APP_ROOT}/bin:${PATH} \
    PIP_NO_CACHE_DIR=false \
    PIPENV_DONT_LOAD_ENV=true \
    PYTHONUNBUFFERED=true

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

COPY apk-packages.txt ${APP_ROOT}/
RUN apk add --no-cache $(grep -vE "^\s*#" ${APP_ROOT}/apk-packages.txt | tr "\r\n" " ") && \
    pip3 install -U pipenv

COPY Pipfile Pipfile.lock ${APP_ROOT}/
RUN pipenv install --system --deploy

COPY package.json yarn.lock ${APP_ROOT}/
RUN yarn install && \
    yarn cache clean

COPY . ${APP_ROOT}/

RUN pip3 install -e ${APP_ROOT} && \
    yarn build && \
    KOBRA_DATABASE_URL=sqlite://:memory: KOBRA_SECRET_KEY=build KOBRA_NO_DATABASE=true django-admin collectstatic --no-input

EXPOSE 80
CMD ["kobra-interface-server"]
