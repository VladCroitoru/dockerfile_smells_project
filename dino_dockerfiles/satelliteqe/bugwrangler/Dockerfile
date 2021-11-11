FROM python:3
LABEL maintainer="omaciel@redhat.com"

WORKDIR /bugwrangler

ADD . /bugwrangler

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV BUGZILLA_USER_NAME=
ENV BUGZILLA_USER_PASSWORD=

# Run bugwrangler when the container launches
ENTRYPOINT [ "bugwrangler" ]
CMD ["--help"]