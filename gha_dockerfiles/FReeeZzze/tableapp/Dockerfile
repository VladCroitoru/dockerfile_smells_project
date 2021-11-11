FROM node:14

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

EXPOSE 3000

RUN npm install

RUN chmod a+x ./run.sh

ENTRYPOINT [ "./run.sh" ]