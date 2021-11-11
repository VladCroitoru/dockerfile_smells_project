#############
## Install ##
#############
FROM node:16 as install

WORKDIR /app

COPY ./package.json .
# COPY ./package-lock.json .
RUN ["npm", "install"]
RUN ["npm", "install", "pm2", "-g"]

#################
## Copy Source ##
#################
FROM install as source
COPY . .

###########
## Build ##
###########
FROM source as build
RUN ["npm", "run", "build"]

##########
## Test ##
##########
# FROM source as test
VOLUME ["/app/coverage", "/app/logs"]
RUN ["npm", "run", "test"]

#############
## Final ##
#############
FROM build as final

COPY --from=build /app/build/ ./
EXPOSE 5000
CMD ["pm2-runtime", "build/src/server.js"]