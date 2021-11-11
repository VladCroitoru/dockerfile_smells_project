# Add swiftclient to the base debian image

# Run a docker registry backed by a Swift datastore.
#
# /usr/bin/docker run --rm \
#   -e SETTINGS_FLAVOR=swift \
#   -e OS_CONTAINER=docker-registry \
#   -e OS_USERNAME=your-username \
#   -e OS_PASSWORD=your-password \
#   -e OS_AUTH_URL=https://identity.api.rackspacecloud.com/v2.0/ \
#   -e OS_REGION_NAME=DFW \
#   -e OS_TENANT_NAME=MossoCloudFS_nnnnn \
#   --name backup-file \
#   wilane/python-swiftclient \
#   swift upload mycontainer myfile-from-volume
#
# /usr/bin/docker run --rm \
#   wilane/python-swiftclient \
#   swift-bench  -A 'AUTH_URL' -U 'subuser:swift' -K 'ULTRASUPERTOPSECRETKKKY' -n 10000 -g 100000 -C 10

FROM debian:latest

# enable backports
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }' /etc/apt/sources.list > /etc/apt/sources.list.d/backports.list
MAINTAINER Ousmane Wilane <wilane@gmail.com>

# Add python swiftclient

RUN DEBIAN_FRONTEND=noninteractive apt update
RUN DEBIAN_FRONTEND=noninteractive apt upgrade -y --no-install-recommends
RUN DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends build-essential git python python-dev python-setuptools python-pip

RUN pip install python-swiftclient
RUN pip install swift-bench
