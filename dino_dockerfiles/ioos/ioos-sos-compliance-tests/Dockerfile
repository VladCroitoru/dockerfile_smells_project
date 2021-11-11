FROM maven:3

ARG TEAMENGINE_VERSION=4.7.1

RUN apt-get update && apt-get install -y dos2unix unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/src

#install teamengine
RUN git clone -b $TEAMENGINE_VERSION --single-branch \
      https://github.com/opengeospatial/teamengine.git teamengine \
    && cd teamengine \
    && mvn clean install \
    && mkdir -p /srv/ioos-sos-compliance-tests/teamengine \
    && unzip -d /srv/ioos-sos-compliance-tests/teamengine teamengine-console/target/teamengine-console-*-bin.zip \
    && cd /usr/local/src \
    && rm -rf /usr/local/src/teamengine \
    && find /srv/ioos-sos-compliance-tests/teamengine -type f -exec dos2unix -q {} +

WORKDIR /srv/ioos-sos-compliance-tests

RUN mkdir -p resources/rdf \
    && cd resources/rdf \
    && wget -O cf-parameter.rdf "http://mmisw.org/ont?form=rdf&uri=http://mmisw.org/ont/cf/parameter" \
    && wget -O ioos-parameter.rdf "http://mmisw.org/ont?form=rdf&uri=http://mmisw.org/ont/ioos/parameter" \
    && wget -O ioos-organization.rdf "http://mmisw.org/ont?form=rdf&uri=http://mmisw.org/ont/ioos/organization" \
    && wget -O ioos-platform.rdf "http://mmisw.org/ont?form=rdf&uri=http://mmisw.org/ont/ioos/platform" \
    && wget -O ioos-sector.rdf "http://mmisw.org/ont?form=rdf&uri=http://mmisw.org/ont/ioos/sector"

COPY m1.0 m1.0
COPY run_tests.sh run_tests.sh
COPY resources/xsd resources/xsd

#Add ioos user
RUN useradd --system --home-dir=/srv/ioos-sos-compliance-tests ioos \
      && chown -R ioos:ioos /srv/ioos-sos-compliance-tests

#Run as ioos user
USER ioos

CMD /srv/ioos-sos-compliance-tests/run_tests.sh
