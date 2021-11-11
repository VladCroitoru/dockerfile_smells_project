# build environment
FROM node:16.9-alpine as build

# Default replace vars for entrypoint
# Should be removed after we able to configure at runtime
ARG REACT_APP_API_HOST=REACT_APP_API_HOST_STRING_REPLACE
ARG REACT_APP_TARA_ADDRESS=REACT_APP_TARA_ADDRESS_STRING_REPLACE
ARG REACT_APP_CLAIM_ADDRESS=REACT_APP_CLAIM_ADDRESS_STRING_REPLACE
ARG REACT_APP_STAKING_ADDRESS=REACT_APP_STAKING_ADDRESS_STRING_REPLACE

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json yarn.lock /app/
RUN yarn install
COPY . /app
RUN SKIP_PREFLIGHT_CHECK=true yarn workspace @taraxa_project/taraxa-ui build
RUN SKIP_PREFLIGHT_CHECK=true yarn workspace @taraxa_project/taraxa-community-site build

# nginx
FROM nginx:1.18-alpine

COPY services/community-site/docker-files/nginx.conf /etc/nginx/conf.d/default.conf
COPY services/community-site/docker-files/entrypoint.sh /entrypoint.sh

COPY --from=build /app/services/community-site/build /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
