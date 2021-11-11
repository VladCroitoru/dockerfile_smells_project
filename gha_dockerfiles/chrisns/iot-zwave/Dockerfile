FROM robertslando/zwave2mqtt:dev@sha256:75abe9232a4e739db2e82d652ffcf56d49fab261c05c9bc82e868ecca9beeab4
LABEL org.opencontainers.image.source https://github.com/chrisns/iot-zwave

WORKDIR /app
COPY . .
RUN npm i --production


ENV AWS_ACCESS_KEY="" \
    AWS_SECRET_ACCESS_KEY="" \
    AWS_IOT_ENDPOINT_HOST="" \
    AWS_REGION="" \
    BUCKET="" \
    BUCKET_KEY="" \
    DEBUG=false \
    DEVICE=/dev/ttyUSB1
WORKDIR /usr/src/app

CMD npm start
