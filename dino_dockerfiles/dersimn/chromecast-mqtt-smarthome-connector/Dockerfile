FROM python:3.8-alpine

# install
RUN mkdir /opt/chromecast-mqtt/
COPY . /opt/chromecast-mqtt/
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# clean
RUN rm requirements.txt

CMD [ "python", "/opt/chromecast-mqtt/connector.py" ]