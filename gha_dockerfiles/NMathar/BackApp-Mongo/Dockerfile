FROM node:lts-buster

# create destination directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# update and install dependency
RUN apt-get update
RUN apt-get install -y mongo-tools

# copy the app, note .dockerignore
COPY . .
COPY docker/start.sh .
RUN chmod +x start.sh
RUN npm install --no-audit

# build necessary, even if no static files are needed,
# since it builds the server as well
# Create fake SECRET_KEY for build
RUN npm run generate:key
RUN npm run build

# expose 3000 on container
EXPOSE 3000

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=3000

# start the app
CMD [ "./start.sh" ]
