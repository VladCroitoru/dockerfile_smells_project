# Node image
FROM node:12

# Create mercurio directory
WORKDIR /mercurio

# Install dependencies
COPY /package*.json /mercurio
RUN npm install

# Bundle app source
COPY . .

# Port map
EXPOSE 3333

# Start server
CMD [ "node", "src/index.ts" ]
