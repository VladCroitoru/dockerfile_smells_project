###
# Nuage VSD provisioner
###

FROM ubuntu:trusty
MAINTAINER Juan Manuel Parrilla Madrid <jparrill@redhat.com>

ENV base_path "/opt/nuage/"
WORKDIR $base_path

RUN apt-get update && \
  apt-get install --no-install-recommends -y software-properties-common python-software-properties python curl && \
  add-apt-repository cloud-archive:kilo && \
  curl --silent --location https://deb.nodesource.com/setup_0.12 | sudo bash - && \
  apt-get -y --force-yes --no-install-recommends install nodejs git python-neutronclient python-glanceclient python-novaclient make && \
  apt-get clean all

RUN npm install --prefix $base_path superagent agentkeepalive netmask express netmask body-parser multer cjson aws-sdk

CMD [""]
ENTRYPOINT ["./rhStart.sh"]

COPY ["*.js", "rhStart.sh", "./"]
COPY ["samples", "./samples"]
