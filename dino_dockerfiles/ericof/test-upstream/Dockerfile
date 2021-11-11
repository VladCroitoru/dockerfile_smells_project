FROM python:3-alpine3.7

LABEL org.label-schema.vendor = "ericof" \
    name="test-upstream" \
    description="Echo server." \
    maintainer="ericof@plone.org"

RUN rundeps=' \
    bash \
    tini \
    ' \
    && adduser -s /bin/false -D -H ttd \
    && apk --no-cache add \
    $rundeps

ADD requirements.txt /
RUN pip install -r requirements.txt
ADD echo.py /

CMD ["python3", "echo.py"]
ENTRYPOINT ["/sbin/tini", "--"]
