FROM node:14.16.0

EXPOSE 8080

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY . .
RUN npm install
RUN npm run build
CMD ["npm", "run", "start"]
