FROM node:alpine
COPY . /wd
RUN cd /wd && npm install && npm run build

FROM node:alpine
COPY --from=0 /wd/dist /app
CMD node /app/server

EXPOSE 8080