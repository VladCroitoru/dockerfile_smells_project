FROM node:7.10.0-slim
MAINTAINER kapeel.sable@gmail.com

RUN mkdir -p /neo-admin/dist \
    && mkdir -p /ohmage-frontends/neo-admin
COPY . /neo-admin
WORKDIR /neo-admin
RUN npm install -g webpack@^1.12.0 \
    && npm install
RUN npm run clean
RUN npm run dist_navbar
RUN rm /neo-admin/dist/assets/app.js.map
RUN mv /neo-admin/dist/* /ohmage-frontends/neo-admin

VOLUME /ohmage-frontends/neo-admin

# Placeholder to override cmd/entrypoint of the parent docker image
ENTRYPOINT echo "Fin."