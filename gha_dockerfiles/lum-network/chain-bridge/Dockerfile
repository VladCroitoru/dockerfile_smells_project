FROM node:12

# Install the packages needed to run Nightmare
RUN apt-get update
RUN apt-get install -y \
  xvfb \
  x11-xkb-utils \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  x11-apps \
  clang \
  libdbus-1-dev \
  libgtk2.0-dev \
  libnotify-dev \
  libgnome-keyring-dev \
  libgconf2-dev \
  libasound2-dev \
  libcap-dev \
  libcups2-dev \
  libxtst-dev \
  libxss1 \
  libnss3-dev \
  gcc-multilib \
  g++-multilib \
  libudev-dev \
  libusb-1.0-0-dev

# Install API
WORKDIR /usr/src/api

COPY package.json ./
COPY tsconfig.json ./
COPY yarn.lock ./
COPY src src/
RUN mkdir output

RUN yarn install
COPY . .
RUN yarn build

EXPOSE 3000

CMD [ "yarn", "start:prod" ]
