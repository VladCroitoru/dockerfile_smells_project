FROM hivesolutions/ubuntu_dev:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

ENV LEVEL INFO
ENV ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV CACHE 86400
ENV INDEX_FILES index.html
ENV LIST_DIRS 0
ENV CORS 1
ENV BASE_PATH /app/dist
ENV NODE_ENV production

ADD .eslintrc.js /app/
ADD index.html.tpl /app/
ADD package.json /app/
ADD webpack.config.js /app/
ADD src /app/src

WORKDIR /app

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y nodejs
RUN pip3 install --upgrade netius
RUN npm install --global yarn
RUN NODE_ENV=dev yarn install
RUN yarn run build

CMD ["/usr/bin/python3", "-m", "netius.extra.filea"]
