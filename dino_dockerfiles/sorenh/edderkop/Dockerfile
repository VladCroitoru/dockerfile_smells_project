FROM alpine
RUN apk --no-cache add py-pip libxml2-dev libxslt-dev build-base python-dev
ADD . /srv
RUN pip install -r /srv/requirements.txt
RUN cd /srv ; python setup.py install
EXPOSE 5000
ENTRYPOINT ["/srv/entrypoint.sh"]
