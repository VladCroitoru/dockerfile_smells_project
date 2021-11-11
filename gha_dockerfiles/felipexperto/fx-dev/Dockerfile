
FROM node:10-alpine AS builder

RUN apk add --no-cache --virtual .gyp python make g++ autoconf automake libtool gcc musl-dev nasm

RUN apk add --no-cache --virtual \  
    .gyp \
    g++ \
    python \
    make \                                                                                        
    gcc \                                                                                         
    autoconf \                                                                                    
    automake \                                                                                    
    musl-dev \                                                                                    
    libtool \                                                                                     
    nasm \                                                                                        
    tiff \                                                                                        
    jpeg \                                                                                        
    zlib \                                                                                        
    zlib-dev \                                                                                    
    file \                                                                                        
    pkgconf \
    libc6-compat \
    libjpeg-turbo-dev \
    libpng-dev

WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install


FROM node:10-alpine AS development

RUN yarn global add gatsby-cli

WORKDIR /app
COPY --from=builder /app/node_modules /app/node_modules
COPY . .

RUN yarn install

EXPOSE 8000
EXPOSE 8001

CMD yarn install; gatsby develop -H 0.0.0.0
