FROM resin/raspberrypi3-node:6.12
#FROM hypriot/rpi-node:argon
RUN [ "cross-build-start" ]
# Create src folder and clone gladys git
RUN mkdir /src && git clone --depth 1 git://github.com/GladysProject/Gladys /src

WORKDIR /src
RUN npm config set unsafe-perm true && npm install
RUN npm install -g grunt
RUN grunt buildProd

# Export listening port
EXPOSE 8080

CMD ["node" ,"app.js"]
RUN [ "cross-build-end" ]
