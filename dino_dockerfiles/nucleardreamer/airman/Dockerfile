FROM oaklabs/oak:3.2.0

WORKDIR /app
COPY . /app

RUN npm i --engine-strict=true --progress=false --loglevel="error" \
    && npm test \
    && npm cache clean

CMD ["/app"]
