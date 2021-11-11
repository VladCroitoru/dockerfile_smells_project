FROM node:14-alpine AS builder

# set working directory
WORKDIR /app

# Copies package.json and yarn.lock to Docker environment
COPY package.json ./
COPY yarn.lock ./

# Install `serve` to run the application.
RUN npm install -g serve
# Installs all node packages
RUN yarn install --frozen-lockfile

# Copies everything over to Docker environment
COPY . .

# Build for production.
RUN yarn build

# Uses port which is used by the actual application
EXPOSE 5000

# Run application
CMD serve -s build