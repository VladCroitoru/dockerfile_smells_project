FROM node:6

EXPOSE 8000:8000

WORKDIR /shintech

COPY . .

RUN rm -rv node_modules build --force && \
  npm install -g webpack && \
  printf "Creating file directories...\n" && \
  mkdir build && \
  mkdir build/static && \
  wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \
  chmod +x /usr/local/bin/dumb-init  

RUN printf "Copying resources...\n"
COPY resources build/resources

RUN printf "Installing dependencies...\n" &&\
  yarn install && \

  printf "Building in progress...\nPlease wait...\n" && \
  webpack --progress --display-reasons --display-modules --display-chunks && \
  npm run build 

CMD dumb-init npm start