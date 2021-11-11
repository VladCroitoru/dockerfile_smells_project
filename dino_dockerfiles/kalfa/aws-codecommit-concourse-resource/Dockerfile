FROM alpine:latest as build

RUN apk --no-cache add python3 && python3 -m ensurepip && \
  pip3 install --upgrade pip setuptools wheel 

COPY setup.py .
COPY README.md .
COPY sqs_resource sqs_resource/

RUN python3 ./setup.py bdist_wheel


FROM concourse/git-resource as git

RUN apk --no-cache add python3 && python3 -m ensurepip && \
  pip3 install --upgrade pip setuptools wheel GitPython

RUN cp -r /opt/resource /opt/original_git && rm /opt/resource/check

WORKDIR /tmp
COPY --from=0 dist/concourse_aws_sqs_notification_resource-* .
RUN pip3 install concourse_aws_sqs_notification_resource-*
# replace only 'check' and re-use 'in' and 'out' from the git-resource
RUN for script in check; do ln -s $(which $script) /opt/resource/; done
