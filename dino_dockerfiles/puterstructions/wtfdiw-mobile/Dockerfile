FROM puterstructions/ionic-inc

RUN mkdir /app

ADD . /app/

WORKDIR /app

RUN npm install && ionic state restore && ionic build

CMD cd www && python -m SimpleHTTPServer 8100
