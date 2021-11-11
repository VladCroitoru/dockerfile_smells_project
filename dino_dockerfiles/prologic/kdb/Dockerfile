FROM crux/python

EXPOSE 8000

ENTRYPOINT ["/usr/bin/kdb"]

RUN ports -u && prt-get depinst git aspell-en enchant

ADD requirements.txt /tmp/requirements.txt
RUN pip install --allow-all-external -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /app
COPY . /app
RUN python setup.py install
