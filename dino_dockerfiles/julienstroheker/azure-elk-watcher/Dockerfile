FROM azuresdk/azure-cli-python

RUN apk update && apk add curl sed

WORKDIR /src

COPY . /src/

ENTRYPOINT [ "./start.sh" ]