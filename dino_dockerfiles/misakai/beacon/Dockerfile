FROM nano/node.js
MAINTAINER Roman Atachiants "roman@misakai.com"

# Extract & Install
COPY . /app
WORKDIR /app

# since we are using nano image, we can't run npm
#RUN npm install

# Beacon Port
EXPOSE 1792

CMD ["/usr/bin/node", "/app/server.js"]