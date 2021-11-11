FROM node:7

RUN ["npm", "install", "-g", "localtunnel"]

ENV LT_HOST https://localtunnel.me

CMD lt --local-host=$LT_LOCAL_HOST --subdomain=$LT_SUBDOMAIN --host=$LT_HOST --port=$LT_PORT
