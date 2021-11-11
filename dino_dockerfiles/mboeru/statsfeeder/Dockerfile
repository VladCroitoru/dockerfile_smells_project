FROM python:2.7
MAINTAINER Marius Boeru <mboeru@gmail.com>


VOLUME /config

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


# Install hass component dependencies
COPY requirements.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

CMD [ "./statsfeeder.py", "-c", "/config" ]
