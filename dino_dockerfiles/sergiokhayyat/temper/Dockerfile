# FROM alpine:3.4
# 
# RUN apk add --no-cache gcc libusb libusb-dev make

FROM ubuntu:12.04

RUN apt-get update && apt-get install -y build-essential libusb-0.1-4 libusb-dev

COPY . /temper

WORKDIR /temper

RUN make clean && make temper_json

CMD [ "./temper_json" ]

