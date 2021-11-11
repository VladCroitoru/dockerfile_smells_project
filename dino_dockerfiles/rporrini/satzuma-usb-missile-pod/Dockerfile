FROM python:2.7.13

RUN \
  apt-get update && \
  apt-get install libusb-dev && \
  pip install urwid

COPY . .

RUN \
  cd pyusb-0.3.1-patched && \
  python setup.py install

CMD [ "python", "./missile.py" ]
