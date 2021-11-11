FROM ubuntu

ENV ZEA_ROOT /usr/src/app/

WORKDIR ${ZEA_ROOT}

RUN apt-get update && apt-get install -y telnet xinetd telnetd

EXPOSE 23

COPY package.json yarn.lock ./

RUN yarn install

COPY ./ ./

CMD ["yarn", "run", "start"]
