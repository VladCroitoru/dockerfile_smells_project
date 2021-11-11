FROM node:14
RUN mkdir -p /app
WORKDIR /app
COPY package*.json /app
RUN npm install && npm i -g nodemon
CMD [ "npm", "run", "run-build" ]
# CMD ["bash"]