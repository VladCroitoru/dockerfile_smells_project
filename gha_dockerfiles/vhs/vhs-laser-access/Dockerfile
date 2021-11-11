#
# Build binary with build dependencies
#
FROM raspbian/stretch AS build

RUN apt-get update && apt-get upgrade -y && apt-get install -y curl git cmake automake autoconf libtool pkg-config build-essential

## Install node and laser-access node modules
RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash -

RUN apt-get update && apt-get install -y nodejs

RUN mkdir -p /var/run/laser-access

WORKDIR /var/run/laser-access

ADD . .

RUN npm install

#
# Build main image
#
FROM raspbian/stretch

RUN apt-get update && apt-get upgrade -y && apt-get install -y curl

RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash -

RUN apt-get update && apt-get install -y nodejs

COPY --from=build /var/run/laser-access /var/run/laser-access

WORKDIR /var/run/laser-access

CMD npm start

EXPOSE 3000
