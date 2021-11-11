FROM node:boron

WORKDIR /usr/src/app

COPY app/ /usr/src/app/

ENV eventHubsNamespace your-eventhub-namespace
ENV eventHubsHubName your-eventhub-name
ENV eventHubsKeyName your-eventhub-keyname
ENV eventHubsKey your-eventhub-key

RUN chmod +x /usr/src/app/run.sh

CMD [ "./run.sh" ]
