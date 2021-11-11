#==================== Building Stage=======================#

# Create the image based on the official Node 10 image from Dockerhub
FROM node:14.15.1-alpine3.12 as build

# Create a new directory
RUN mkdir -p /app

# Change directory so that our commands run inside this new directory
WORKDIR /app

# Copy dependency definitions
COPY package.json yarn.lock /app/

# Install dependencies using npm
RUN yarn install --frozen-lockfile

# Get all the code needed to run the ap
COPY . /app/

#Build the app
RUN yarn run build

#==================== Setting up stage ====================#

# Create image based on the official nginx - Alpine image
FROM nginx:1.13.7-alpine

COPY --from=build /app/build /usr/share/nginx/html
# nginx.conf to configure nginx because of react routing
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]