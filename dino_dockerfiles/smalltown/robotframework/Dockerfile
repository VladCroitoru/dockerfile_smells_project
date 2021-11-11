FROM ubuntu:xenial

RUN echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu trusty main" > /etc/apt/sources.list.d//mozillateam-firefox-next-trusty.list && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE49EC21 && apt-get update && apt-get install -y firefox xvfb python-pip wget fonts-wqy-zenhei && pip install --upgrade pip

RUN wget -qO- https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz | tar -xz -C /usr/bin/

COPY requirements.txt /root/requirements.txt

RUN pip install --pre -r /root/requirements.txt

CMD (Xvfb :10 -ac & export DISPLAY=:10; robot -d /root/test/output -v PHASE:$PHASE -v PROJECT:$PROJECT -v VERSION:$VERSION -v RUNTIME:container /root/test/tests)
