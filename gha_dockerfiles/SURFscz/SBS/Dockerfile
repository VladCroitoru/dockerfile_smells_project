    # Stage 1. - Client build environment
FROM node:8 as yarn-deps

WORKDIR /opt/app

COPY client/package.json client/yarn.lock ./
RUN yarn

COPY client/ ./
RUN yarn build
RUN CI=true yarn test

# Stage 2. - Client build
FROM python:3.6

WORKDIR /opt/app

RUN apt-get update && apt-get install -y gettext-base nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY server/ server/
RUN pip install --no-cache-dir -r server/requirements/base.txt
COPY --from=yarn-deps /opt/app/build /var/www
COPY etc/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
