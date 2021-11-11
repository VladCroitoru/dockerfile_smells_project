# Temporary build image
FROM node:9.5.0-slim AS builder

ADD app /calendar-monitor

WORKDIR /calendar-monitor/client
RUN npm install --silent
RUN npm run build

WORKDIR /calendar-monitor
RUN npm install --silent

# Production
FROM node:9.5.0-slim

COPY --from=builder /calendar-monitor /calendar-monitor
ONBUILD ADD config.json /calendar-monitor/config.json
EXPOSE 3001
CMD [ "node", "/calendar-monitor/app.js"]