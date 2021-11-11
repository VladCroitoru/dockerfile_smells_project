FROM python:3

COPY req.txt /srv/req.txt
RUN pip install -r /srv/req.txt

EXPOSE 5555

COPY *.py /srv/
COPY settings.default.py /srv/settings.py
COPY templates/ /srv/templates
COPY static/ /srv/static

VOLUME /srv/gif

WORKDIR /srv/
CMD python server.py
