FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 0

COPY . /aws-snapshot-recovery/
RUN pip3 install -r /aws-snapshot-recovery/requirements && \
    apk update && \
    apk --no-cache add openssh    

ENTRYPOINT ["/aws-snapshot-recovery/bin/aws-snapshot-recovery"]
