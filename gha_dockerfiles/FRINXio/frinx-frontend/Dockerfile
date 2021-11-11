FROM node:14-alpine as build

WORKDIR /frinx-frontend
COPY . .

# adding yarn + installing a bunch of stuff as a workaround for alpine bug suggested here https://gitlab.alpinelinux.org/alpine/aports/-/issues/11615
RUN apk add -U --no-cache nghttp2-dev nodejs npm unzip yarn git 

RUN yarn install --frozen-lockfile && yarn cache clean

# TODO there should be a build for whole repo, not an individual project
RUN cd  /frinx-frontend/packages/frinx-dashboard && \
        cp .env.example .env && \
        yarn build


FROM nginxinc/nginx-unprivileged:alpine as server

EXPOSE 8888

WORKDIR /frinx-frontend

USER root

RUN rm -rf /usr/share/nginx/html/* && \
        rm -rf /etc/nginx/nginx.conf
        
# TODO we should have static code generated for the whole repo, not an individual project
COPY --from=build /frinx-frontend/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /frinx-frontend/packages/frinx-dashboard/build /usr/share/nginx/html

RUN touch /var/run/nginx.pid && \
        touch /var/log/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid && \
        chown -R nginx:nginx /var/log/nginx.pid && \
        chown -R nginx:nginx /usr/share/nginx/html && \
        chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d && \
        chown -R nginx:nginx /etc/nginx/nginx.conf && \
        chown -R nginx:nginx /usr/share/nginx/html
             
USER nginx