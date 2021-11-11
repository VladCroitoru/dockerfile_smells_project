FROM node:10-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install --only=production
# If you are building your code for production
# RUN npm ci --only=production

#RUN npm audit fix
RUN export NODE_ENV=production

ENV PORT=8080
ENV BACKEND_URL="svc-awesome-clinic-backend"
# Bundle app source
COPY . .

EXPOSE 8080

CMD [ "npm", "start" ]