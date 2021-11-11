FROM registry.access.redhat.com/ubi8/python-36:latest

LABEL name="f8analytics pypi insights service" \
      description="Fabric8 analytic python insights service for recommendation." \
      email-ids="dhpatel@redhat.com" \
      git-url="https://github.com/fabric8-analytics/f8a-pypi-insights" \
      git-path="/" \
      target-file="Dockerfile" \
      app-license="GPL-3.0"

ENV LANG=en_US.UTF-8 PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt /opt/app-root

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r /opt/app-root/requirements.txt
RUN pip3 install --no-cache-dir Cython==0.29.1 && pip3 install --no-cache-dir hpfrec==0.2.2.9

COPY ./src /opt/app-root/src/src
ADD ./entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["bash", "/bin/entrypoint.sh"]
