#############
### build ###
#############

# base image
FROM docker-registry.groupclaes.be/node-npm as build

# install chrome for protractor tests
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
# RUN apt-get update && apt-get install -yq google-chrome-stable

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install

# add app
COPY . /app

# run tests
# RUN ng test --watch=false
# RUN ng e2e --port 4202

# generate build
RUN ng build --configuration production --output-path=dist

############
### prod ###
############

# base image
FROM docker-registry.groupclaes.be/nginx:latest

#remove all content form html
RUN rm -rf /usr/share/nginx/html/*

# copy artifact build from the 'build environment'
COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf

# expose port 80
EXPOSE 80