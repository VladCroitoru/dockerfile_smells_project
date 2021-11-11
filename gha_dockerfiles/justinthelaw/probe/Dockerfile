FROM ubuntu:20.04 AS BUILD_STAGE

RUN apt-get update -q && apt-get clean
RUN apt-get install curl -y && (curl https://install.meteor.com/ | sh)

WORKDIR /app
COPY . .

RUN ./scripts/build-prod.sh

# If you don't have access to Iron Bank, just use the node:14.16.1 image from Docker
FROM registry1.dso.mil/ironbank/opensource/nodejs/nodejs14@sha256:1aa1227b8c3b3adf19280ce88a67ecf696d598ae94c8dbd3253415aa5efb8983

USER root

WORKDIR /app
COPY --from=BUILD_STAGE /app/build/bundle .
RUN cd /app/programs/server && npm install --production && npm cache clean --force

EXPOSE 3000

# Run the database migration script before starting the program.
ENTRYPOINT ["node", "/app/main.js", "--v"]
