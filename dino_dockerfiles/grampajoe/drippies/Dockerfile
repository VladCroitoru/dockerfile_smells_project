FROM python:3.4

RUN curl https://nodejs.org/dist/v0.12.7/node-v0.12.7-linux-x64.tar.gz > /node.tar.gz && \
      mkdir /opt/node && tar --strip-components=1 -zxf /node.tar.gz -C /opt/node

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY js/package.json /app/js/package.json
RUN cd /app/js && \
    /opt/node/bin/npm install && \
    /opt/node/bin/npm install -g browserify

COPY . /app
RUN cd /app/js && \
    PATH=$PATH:/opt/node/bin npm run-script build && \
    rm -rf /opt/node /app/js/node_modules

WORKDIR /app

ENV PORT=5000
ENV FORECASTIO_API_KEY='your-key-here'

EXPOSE 5000

CMD gunicorn drippies:app -b 0.0.0.0:$PORT --access-logfile=- --error-logfile=- --log-file=- -w 2 -k eventlet
