# Intialize Container and install NodeJs
FROM node:14-alpine
# Set Env in Production mode
ENV NODE_ENV=production
# Working Directory of Container
WORKDIR /usr/src/app
# Copy File to container
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
# Intialize node_modules in container
RUN npm install --production --silent && mv node_modules ../
# Copy remainig Code to the container
COPY . .
# PORT where Run the Demon server
EXPOSE 3000
# Enterence commond of the Container
CMD ["npm", "start"]