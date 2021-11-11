##############
# BuildStage #
##############

# pull offical base image
FROM node:14.15.4-alpine as build-stage

# set working dir
WORKDIR /app
COPY . .

RUN yarn install
RUN yarn run build

###########
#  FINAL  #
###########

# base image
FROM nginx:1.19.4-alpine as production-stage

# copy static files
COPY --from=build-stage /app/build /usr/share/nginx/html

# export port
EXPOSE 80

# run nginx
CMD ["nginx", "-g", "daemon off;"]
