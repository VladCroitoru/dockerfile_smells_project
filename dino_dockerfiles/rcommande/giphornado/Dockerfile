FROM alpine:3.4


RUN apk add --no-cache python3
RUN /usr/bin/pip3 install tornado
ADD giphornado.py /giphornado.py

EXPOSE 8888

CMD python3 giphornado.py
