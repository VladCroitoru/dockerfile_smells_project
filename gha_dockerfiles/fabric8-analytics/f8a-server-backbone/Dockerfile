FROM registry.access.redhat.com/ubi8/python-36:latest

LABEL name="f8analytics backbone services" \
      description="Stack aggregation and recommendation service." \
      email-ids="yzainee@redhat.com,deepshar@redhat.com" \
      git-url="https://github.com/fabric8-analytics/f8a-server-backbone" \
      git-path="/" \
      target-file="Dockerfile" \
      app-license="GPL-3.0"

ENV LANG=en_US.UTF-8 PYTHONDONTWRITEBYTECODE=1

RUN pip3 install --upgrade --no-cache-dir pip

COPY ./requirements.txt /opt/app-root
RUN pip3 install --no-cache-dir -r /opt/app-root/requirements.txt

COPY ./src /opt/app-root/src/src
ADD scripts/entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["bash", "/bin/entrypoint.sh"]
