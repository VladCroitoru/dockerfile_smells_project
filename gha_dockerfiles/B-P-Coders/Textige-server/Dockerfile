FROM alpine:latest

RUN apk add --update nodejs npm
RUN mkdir /home/textige
WORKDIR /home/textige
ADD . /home/textige
RUN npm install
CMD ["sh", "-c", "npm run dev"]