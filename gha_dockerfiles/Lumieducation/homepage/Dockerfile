# We use a build image to keep the final image as clean as possible

FROM node:16 AS BUILD_IMAGE

# install 
RUN npm install -g clean-modules
WORKDIR /app
COPY ./package*.json /app/
RUN npm ci 

COPY . /app/

# build
RUN npm run build

# remove development dependencies
RUN npm prune --production

# run clean-modules
RUN clean-modules --yes

FROM node:16-alpine

WORKDIR /app

# copy from build image
COPY --from=BUILD_IMAGE /app/build ./build
COPY --from=BUILD_IMAGE /app/node_modules ./node_modules
COPY --from=BUILD_IMAGE /app/views ./views
COPY --from=BUILD_IMAGE /app/public ./public
COPY --from=BUILD_IMAGE /app/locales ./locales

EXPOSE 8080

CMD [ "node", "build/app.js" ]