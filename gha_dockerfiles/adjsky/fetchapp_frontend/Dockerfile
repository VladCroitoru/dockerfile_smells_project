FROM alpine:3.14
RUN apk add --no-cache npm
COPY . /source_code
WORKDIR /source_code
RUN npm i
CMD npm run build && npm start