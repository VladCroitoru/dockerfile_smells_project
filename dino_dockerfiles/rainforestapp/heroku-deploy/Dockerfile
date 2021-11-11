FROM ubuntu:17.10
RUN apt-get update -y && apt-get install -y curl wget jq git

RUN mkdir scripts
COPY scripts/ ./scripts/
RUN sh ./scripts/install.sh
ENTRYPOINT ["heroku"]
