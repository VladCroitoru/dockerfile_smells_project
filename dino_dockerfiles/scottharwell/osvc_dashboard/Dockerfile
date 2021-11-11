FROM alpine:3.6

# Update
RUN apk add --update nodejs nodejs-npm

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json .
# For npm@5 or later, copy package-lock.json as well
# COPY package.json package-lock.json .

# Install NPM Packages
RUN npm install

# Bundle app source
COPY . .

# Run TypeScript Transpiler
RUN node_modules/typescript/bin/tsc

# Use port 3000 for our app
EXPOSE  3000

CMD ["npm", "start"]
