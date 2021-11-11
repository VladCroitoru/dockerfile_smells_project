# CMD

# docker build --progress=plain -f ./Dockerfile . 
# docker build -f ./Dockerfile .  

# containerID

# docker exec -it 28a91698ebea5a79f7ed9b887a6960fdb359cf7f9df1b849fbef30374e008f12 /bin/sh 
# docker exec -it 9535b9d0b723 /bin/sh

# docker run --publish 80:80 91baeee62323 

# To get images
# docker images 

# To get container
# docker ps

# stop a container
# docker container stop container-id

# remove a container
# docker container rm container-id

# remove a image
# docker rmi -f image-id (force mode)




# a custom Docker Image with this Dockerfile for live classes
FROM ubuntu:18.04

# build environment
FROM node:14 as build

RUN mkdir /app
# A directory within the virtualized Docker environment
# Becomes more relevant when using Docker Compose later
WORKDIR /app

# ENV PATH /app/node_modules/.bin:$PATH

# Copies package.json to Docker environment
COPY package.json ./
# COPY package-lock.json ./

# Installs all node packages
RUN npm install

# Copies everything over to Docker environment
COPY . ./

# Runs the application
RUN npm run build-liveclasses:staging
# CMD ["npm", "run build:staging"]


#Create a new container from a linux base image that has the aws-cli installed
FROM amazon/aws-cli

RUN aws configure set preview.cloudfront true

RUN aws configure set aws_access_key_id XXXXXXXXXXXX
RUN aws configure set aws_secret_access_key XXXXXXXXXXXXXXXX
RUN aws configure set default.region ap-xxxxxxxxxx-1

#Set the default command of this container to push the files from the working directory of this container to our s3 bucket 
# RUN aws s3 sync / s3://paas-institute-staging/teach/liveclasses --acl public-read
COPY --from=build /app/build /usr/share/build
RUN aws s3 cp /usr/share/build/ s3://xxxxxxxxx/xxxxxx/xxxxxxx --recursive --acl public-read

# production environment
FROM nginx:stable-alpine

# Copies build to nginx html
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html


# Uses port which is used by the actual application
EXPOSE 80

# CMD ["nginx", "-c", "/app/nginx.conf"]
CMD ["nginx", "-g", "daemon off;"]

