FROM node

# Create Directory for the Container
WORKDIR /usr/app
# Only copy the package.json file to work directory
COPY package*.json ./
# Install all Packages
RUN npm install

COPY . .

RUN npm run build
COPY .env ./build/
WORKDIR ./build

EXPOSE 4000
CMD ["npm", "start"]
