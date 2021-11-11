FROM mariadb

RUN apt-get update -yq
RUN apt-get install apt-transport-https wget -yq
RUN wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -
RUN echo "deb http://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list
RUN apt-get update -yq
RUN apt-get install ca-certificates cf-cli zip sudo build-essential wget curl jq -yq
RUN cf install-plugin https://swisscom-plugin.scapp.io/linux64/swisscom-plugin -f