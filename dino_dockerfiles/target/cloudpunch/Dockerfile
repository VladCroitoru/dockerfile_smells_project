# Create the CloudPunch egg
FROM python:2 AS build
RUN mkdir -p /opt/cloudpunch
COPY . /opt/cloudpunch
WORKDIR /opt/cloudpunch
RUN python setup.py bdist_egg

# Install required packages and the CloudPunch egg
FROM python:2
RUN apt-get update && \
    apt-get install -y redis-server && \
    apt-get clean
WORKDIR /root/
COPY --from=build /opt/cloudpunch/dist/*.egg ./
RUN easy_install $(ls *.egg)
CMD ["/bin/bash"]
