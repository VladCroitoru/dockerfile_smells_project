FROM nikolaik/python-nodejs:latest

USER root

# Create app directory
WORKDIR /app

# Install python dependencies
RUN pip install scrapy
RUN pip install scrapy_proxies
RUN pip install scrapy-fake-useragent

# Install node dependencies
COPY package*.json ./
RUN yarn install

# Bundle app source
COPY . /app

EXPOSE 3333
CMD ["yarn", "watch:dev"]