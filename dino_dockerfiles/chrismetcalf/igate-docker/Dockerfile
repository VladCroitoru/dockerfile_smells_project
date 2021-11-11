FROM marcelmaatkamp/gnuradio

RUN apt-get update \
  && apt-get install -y libasound2-dev build-essential git curl

RUN cd /usr/src \
  && curl -L https://github.com/wb2osz/direwolf/archive/1.4.tar.gz | tar -zxf - \
  && cd direwolf-1.4 \
  && make \
  && make install

RUN mkdir /app
COPY direwolf.sh /app/direwolf.sh
RUN chmod +x /app/direwolf.sh

ENTRYPOINT ["/app/direwolf.sh"]
