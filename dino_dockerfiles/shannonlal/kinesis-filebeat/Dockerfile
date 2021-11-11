FROM node:7.4
MAINTAINER shannonlal

COPY . /kinesis-filebeat
WORKDIR kinesis-filebeat

RUN npm install -g pm2
RUN pm2 -v
RUN npm install --no-optionals --ignore-scripts
RUN pm2 set pm2-logrotate:max_size 10M
CMD pm2 start src/index.js --no-daemon -x -- ${LOG_STREAM_FILE} ${PUSH_INTERVAL} ${AWS_ACCESS_KEY} ${AWS_SECRET_KEY} ${AWS_KINESIS_STREAM_NAME} ${REGION}
