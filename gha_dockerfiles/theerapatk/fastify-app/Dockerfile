FROM node:14.17-slim as dependency
WORKDIR /opt/app

COPY backend/package.json /opt/app/backend/package.json
WORKDIR /opt/app/backend
RUN npm install

FROM node:14.17-slim as build
WORKDIR /opt/app
COPY  --from=dependency /opt/app/backend/node_modules /opt/app/backend/node_modules

COPY backend/ /opt/app/backend/
WORKDIR /opt/app/backend
RUN npm run build

FROM node:14.17-slim as runtime
RUN apt update && \
    apt install -y tzdata

ENV TZ=Asia/Bangkok

WORKDIR /opt/app
COPY  --from=dependency /opt/app/backend/node_modules /opt/app/node_modules
COPY  --from=build /opt/app/backend/dist/ /opt/app/

CMD node index
