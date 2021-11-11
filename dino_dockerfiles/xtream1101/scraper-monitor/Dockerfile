FROM alpine:3.4


RUN apk add --no-cache python3 python3-dev postgresql-dev gcc musl-dev

# Copy app over
COPY . /src/

# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r /src/requirements.txt

WORKDIR /src/

RUN chmod +x docker-entrypoint.sh

EXPOSE 5001

ENTRYPOINT ["/src/docker-entrypoint.sh"]
