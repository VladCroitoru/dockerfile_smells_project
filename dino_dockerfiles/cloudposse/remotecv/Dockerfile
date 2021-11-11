FROM python:2

VOLUME /logs
VOLUME /data

ENV HOME /app
ENV SHELL bash
ENV WORKON_HOME /app

ADD *.txt /tmp/

WORKDIR /app

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y autoremove && \
    xargs apt-get -y -q install < /tmp/apt.txt && \
    apt-get clean && \
    pip install --no-cache-dir -r /tmp/pip.txt && \
    ln /usr/lib/python2.7/dist-packages/cv2.x86_64-linux-gnu.so /usr/local/lib/python2.7/cv2.so && \
    ln /usr/lib/python2.7/dist-packages/cv.py /usr/local/lib/python2.7/cv.py && \
    ln /dev/null /dev/raw1394 && \
    rm -f /tmp/*.txt

ADD start /start
ENTRYPOINT ["/start"]

CMD ["remotecv"]
