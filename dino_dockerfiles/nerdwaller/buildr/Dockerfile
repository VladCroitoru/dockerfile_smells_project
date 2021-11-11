FROM docker:1.12

RUN apk add -U python3
COPY . /app
WORKDIR /app
RUN python3 setup.py install
ENTRYPOINT ["buildr"]
CMD ["--help"]
