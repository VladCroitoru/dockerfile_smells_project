FROM python:3.6-alpine3.6

ENV PYTHONUNBUFFERED=1

RUN pip3 install homeassistant \
  paho-mqtt==1.3.1 \
  sqlalchemy==1.2.2 \
  aiohttp_cors==0.6.0 \
  home-assistant-frontend==20180209.0 \
  user-agents==1.1.0 \
  xmltodict

EXPOSE 8123

RUN mkdir /config && chmod g+rw /config && \
  ln -s /media/config/configuration.yaml /config/configuration.yaml && \
  ln -s /media/storage/home-assistant_v2.db /config/home-assistant_v2.db
  

CMD ["--config", "/config"]
ENTRYPOINT ["hass"]

#COPY ttt.py /ttt.py
#ENTRYPOINT ["python3", "ttt.py"]
