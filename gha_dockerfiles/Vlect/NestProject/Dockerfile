FROM node:14.17.1

# Create app directory, this is our container/in our image
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# Run npm ci --only=production

# Bundle app source
COPY . .

ENV DB_HOST=127.0.0.1
ENV DB_PORT=3306
ENV DB_USERNAME=user
ENV DB_PASSWORD=password
ENV DB_ONE_NAME=db_one_name
ENV DB_TWO_NAME=db_two_name
ENV DB_ROOT_PASSWORD=db_two_name

EXPOSE 3000
CMD [ "npm", "start" ]
