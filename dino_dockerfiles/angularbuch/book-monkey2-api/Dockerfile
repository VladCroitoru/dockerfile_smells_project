FROM nodesource/node:6.3.0

# 1st adding dependencies (this way you don't rebuild your modules each time you re-build your container)
RUN npm install -g yarn

ADD package.json .
ADD yarn.lock .
 
RUN yarn install

# 2n adding app code to the container
ADD . .

EXPOSE 3000
CMD ["npm", "run", "startForever"]
