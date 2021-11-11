FROM node:10-alpine

RUN apk --no-cache add shadow \                                                                   
    gcc \                                                                                         
    musl-dev \                                                                                    
    autoconf \                                                                                    
    automake \                                                                                    
    make \                                                                                        
    libtool \                                                                                     
    nasm \                                                                                        
    tiff \                                                                                        
    jpeg \                                                                                        
    zlib \                                                                                        
    zlib-dev \                                                                                    
    file \                                                                                        
    pkgconf \
	sudo

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./

RUN echo root:RoAot321 | /usr/sbin/chpasswd
RUN echo node:node123 | /usr/sbin/chpasswd
RUN usermod -u 1003 node

USER node

RUN npm install

COPY --chown=node:node . .

EXPOSE 3000

CMD [ "npm", "start" ]