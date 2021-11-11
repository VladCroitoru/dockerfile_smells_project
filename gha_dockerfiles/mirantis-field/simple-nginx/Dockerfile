# Base image from Docker Hub: 
# https://hub.docker.com/_/nginx/
FROM nginx:1.19.10-alpine

COPY html /usr/share/nginx/html

HEALTHCHECK --interval=5s --timeout=5s CMD wget -q -O - -U "healthcheck" http://localhost:80/ || exit 1

# The following lines are inherited from nginx base image:
# https://github.com/nginxinc/docker-nginx/blob/master/mainline/alpine/Dockerfile
##########################################################
#EXPOSE 80

#CMD ["nginx", "-g", "daemon off;"]
