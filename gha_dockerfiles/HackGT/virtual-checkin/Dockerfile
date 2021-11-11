# Build container
FROM node:12-alpine AS build

WORKDIR /usr/src/virtual-checkin/
COPY . /usr/src/virtual-checkin/

WORKDIR /usr/src/virtual-checkin/server
RUN npm install

WORKDIR /usr/src/virtual-checkin/client
RUN npm install && npm run build

# Runtime container
FROM node:12-alpine

COPY --from=build /usr/src/virtual-checkin/server/ /usr/src/virtual-checkin/server/
COPY --from=build /usr/src/virtual-checkin/client/ /usr/src/virtual-checkin/client/

WORKDIR /usr/src/virtual-checkin/server/

ENV TZ="America/New_York"

EXPOSE 3000
CMD ["npm", "start"]
