from node:alpine

#run npm install -g npm

add . /app
workdir /app
run npm install .

# Mount over /data/tmproxy.yml or set var TMPROXY_CONFIG.
add tmproxy.docker.yml /data/tmproxy.yml
env TMPROXY_CONFIG /data/tmproxy.yml

# Port 2000 is the proxy port and 2001 is the control port.
# (2000 is safe to map but 2001 should be internal)
expose 2000/tcp 2001/tcp

cmd node server.js
