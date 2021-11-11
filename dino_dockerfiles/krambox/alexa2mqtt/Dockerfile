#
# ---- Dependencies ----
FROM mhart/alpine-node:10 AS dependencies
RUN apk add --no-cache python build-base

WORKDIR /root/app
COPY package.json .
COPY package-lock.json .

# install node packages
RUN npm set progress=false && npm config set depth 0
RUN npm install --only=production 
# copy production node_modules aside
RUN cp -R node_modules prod_node_modules

#
# ---- Release ----
FROM mhart/alpine-node:base-10
WORKDIR /root/app
# copy production node_modules
COPY --from=dependencies /root/app/prod_node_modules ./node_modules
# copy app sources
COPY package.json .
COPY config.js .
COPY alexa2mqtt.js .
COPY setup.xml .
VOLUME ["/data"]
EXPOSE 1900/udp 
EXPOSE 8082
CMD ./alexa2mqtt.js 