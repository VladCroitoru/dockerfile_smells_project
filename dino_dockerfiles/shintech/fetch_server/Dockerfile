FROM node:6

EXPOSE 8001:8001

WORKDIR /shintech

COPY . .

RUN echo "Starting..." && \
  npm install -g webpack && \
  rm -rv node_modules build --force && \
  printf "Creating file directories...\n" && \
  mkdir build && \
  mkdir build/static 
  
RUN printf "Copying resources...\n"
COPY resources build/resources

RUN printf "Installing dependencies...\n" &&\
  yarn install && \

  printf "Building in progress...\nPlease wait...\n" && \
  webpack && \
  npm run build 

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \
 chmod +x /usr/local/bin/dumb-init

CMD dumb-init npm start