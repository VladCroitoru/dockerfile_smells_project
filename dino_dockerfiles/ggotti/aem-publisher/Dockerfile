# DOCKER-VERSION 1.0.1
FROM ggotti/aem-base
MAINTAINER ggotti

#Copies required build media
ONBUILD ADD cq-publish-4503.jar /aem/cq-publish-4503.jar
ONBUILD ADD license.properties /aem/license.properties

# Extracts AEM
ONBUILD WORKDIR /aem
ONBUILD RUN java -XX:MaxPermSize=256m -Xmx1024M -jar cq-publish-4503.jar -unpack -r publish -p 4503

# Add customised log file, to print the logging to standard out.
ONBUILD ADD https://raw.githubusercontent.com/ggotti/aem_author/master/org.apache.sling.commons.log.LogManager.config /aem/crx-quickstart/install

# Installs AEM
ONBUILD RUN python aemInstaller.py -i cq-publish-4503.jar -r publish -p 4503

ONBUILD WORKDIR /aem/crx-quickstart/bin
#Replaces the port within the quickstart file with the standard publisher port
ONBUILD RUN cp quickstart quickstart.original
ONBUILD RUN cat quickstart.original | sed "s|4502|4503|g" > quickstart


EXPOSE 4503 8000
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
