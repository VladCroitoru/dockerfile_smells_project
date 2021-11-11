 
#
# ---- Build ----
FROM mhart/alpine-node:8  AS dependencies
WORKDIR /root/app

#RUN apk add --no-cache  python build-base
# install node packages
RUN npm set progress=false && npm config set depth 0
RUN npm install hue2mqtt.js --only=production 
# copy production node_modules aside
RUN cp -R node_modules prod_node_modules

#
# ---- Release ----
FROM mhart/alpine-node:base-8
WORKDIR /root/app
# copy production node_modules
COPY --from=dependencies /root/app/prod_node_modules ./node_modules
# copy app sources
VOLUME ["/root/.hue2mqtt"]
CMD ./node_modules/hue2mqtt.js/index.js