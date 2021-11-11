FROM node:16 as build-stage
# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install --production

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app 
RUN npm run build

#deploy stage
FROM node:16-slim

WORKDIR /app

# install simple http server for serving static content
RUN npm install -g http-server
COPY --from=build-stage /app/dist dist

# copy entrypoint script as /entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh
EXPOSE 8080

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
