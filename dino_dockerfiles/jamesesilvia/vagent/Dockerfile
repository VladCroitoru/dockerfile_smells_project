# nodejs image
FROM node:latest

# working directory
WORKDIR /home/app

# put all code in that container
ADD . /home/app

# Install things we need
RUN \
  npm install -g bower && \
  npm install && \
  bower install --config.interactive=false --allow-root
 
# let docker know what port
EXPOSE 9000

# run our server
CMD ["node", "server/app.js"]
