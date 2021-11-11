# OS preparation
FROM alpine:latest
RUN apk update && apk upgrade
RUN apk add git nodejs yarn


# Running the app
WORKDIR /root
RUN git clone https://github.com/akayami/kidsmath.git
WORKDIR /root/kidsmath
RUN yarn install
CMD yarn start