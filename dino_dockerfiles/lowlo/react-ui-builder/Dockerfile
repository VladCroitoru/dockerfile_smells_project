FROM debian:stable


RUN apt-get update && apt-get install -y curl
RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get install -y nodejs build-essential

RUN npm install react-ui-builder -g

CMD ["react-ui-builder"]

EXPOSE 2222

