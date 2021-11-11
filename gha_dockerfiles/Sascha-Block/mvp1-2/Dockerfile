# choose node version
FROM node:15.12.0-alpine

# create working directory
WORKDIR .

# copy everything needed, note .dockerignore
COPY . .

# install dependencies
RUN yarn install

# build everything
RUN yarn build

# expose port 3000 on container
EXPOSE 3000

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=3000

# start the app
CMD [ "yarn", "start" ]
