FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server
RUN yes | apk add git


# make the 'app' folder the current working directory
RUN git clone https://github.com/avionic-iot-aviot/frontend app
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
#COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
#COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "./start.sh" ]
