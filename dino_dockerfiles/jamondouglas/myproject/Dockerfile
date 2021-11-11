FROM node:0.12-onbuild

# Bundle app source
COPY . /src
# Install app dependencies
RUN cd /src; npm install --production

CMD ["node", "/src/app.js"]
EXPOSE 3000
