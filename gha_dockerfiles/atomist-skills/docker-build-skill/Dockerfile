# Set up build
FROM node:lts@sha256:683b8ea4ebc033a0f9060501fc31c1481d3f7232cc032851abbd8cc8d91fdff7 AS build

RUN mkdir -p /atm/home/output

WORKDIR /usr/src

COPY . ./ 

RUN npm ci --no-optional && \
    npm run compile && \
    rm -rf node_modules .git
 
# Set up running image     
FROM atomist/skill:node14@sha256:ece1ae57959d60970e895928b04d0bbc84a3c448b1f99c7e1add23e525a1d013

RUN apt-get update && \
    apt-get install -y curl=7.74.0-1ubuntu2.3 libpcsclite-dev=1.9.1-1 && \
    curl -LO https://github.com/sigstore/cosign/releases/download/v0.4.0/cosign-linux-amd64 && \
    chmod +x cosign-linux-amd64 && \
    mv cosign-linux-amd64 /usr/local/bin/cosign && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/cache/apt /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    cosign version

WORKDIR "/skill"

COPY package.json package-lock.json ./

RUN npm ci --no-optional \
    && rm -rf /root/.npm

COPY --from=build /usr/src/ .

ENTRYPOINT ["node", "--no-deprecation", "--trace-warnings", "--expose_gc", "--optimize_for_size", "--always_compact", "--max_old_space_size=512", "/skill/bin/start.js"]
CMD ["run"]
