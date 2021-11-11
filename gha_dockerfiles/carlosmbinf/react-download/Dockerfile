# Pull base image.
FROM mhart/alpine-node:4
# Install build tools to compile native npm modules
RUN apk add — update build-base python
# Create app directory
RUN mkdir -p /usr/app
COPY . /usr/app
RUN cd /usr/app/programs/server && npm install — production
WORKDIR /usr/app
ENV PORT=3000
ENV MONGO_URL=mongodb://localhost:3001
ENV ROOT_URL=http://localhost:3000/
CMD [ "npm", "start" ]
EXPOSE 3000