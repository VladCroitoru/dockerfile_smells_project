# Docker for Production

# This file will be look by AWS Elasticbeanstalk docker plataform  (Dockerfile)

# when travis ci deploy the app to AWS Elastic Bean Stalk

# Specify a base image
FROM node:alpine as builder

# Work directory in the container
WORKDIR '/app'

# Copy my 'package.json' to '/app' directory in the container
COPY package.json .

# Pulling the dependencies
RUN npm install

# Copy over all the source code with dependencies to the container 
COPY . .

#Build compact version for production ( inside container '/app/build')
RUN npm run build



FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html

#For AWS Elasticbeanstalk exposing the app to port 80
EXPOSE 80 

