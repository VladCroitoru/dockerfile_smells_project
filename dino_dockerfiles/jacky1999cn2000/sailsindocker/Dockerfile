FROM node:4

RUN npm install sails -g
RUN npm install nodemon -g

# add only package.json so docker uses the cache to build image except when a dependency has changed
ADD package.json /src/package.json

RUN cd src && npm install

# add remaining source code to container so we can actually run the app
# we should remove node_module folder when building image
COPY . /src

WORKDIR /src

EXPOSE 1337

# run different task based on passed in ENV 
CMD ["./cmd.sh"]
