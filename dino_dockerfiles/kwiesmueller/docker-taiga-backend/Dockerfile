FROM python:3.4
MAINTAINER Benjamin Borbe <bborbe@rocketnews.de>
ENV VERSION latest

RUN set -x \
	&& DEBIAN_FRONTEND=noninteractive apt-get update --quiet \
	&& DEBIAN_FRONTEND=noninteractive apt-get upgrade --quiet --yes \
	&& DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes --no-install-recommends apt-transport-https ca-certificates gettext postgresql wget \
	&& DEBIAN_FRONTEND=noninteractive apt-get autoremove --yes \
	&& DEBIAN_FRONTEND=noninteractive apt-get clean

RUN git clone -b stable --single-branch --depth 1 https://github.com/taigaio/taiga-back.git /taiga

ENV HOME /taiga
WORKDIR /taiga

RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python

RUN pip install html5lib==1.0b8
RUN pip install --no-cache-dir -r requirements.txt

COPY local.py /taiga/settings/local.py.template

RUN python manage.py compilemessages

EXPOSE 8000

COPY entrypoint.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
