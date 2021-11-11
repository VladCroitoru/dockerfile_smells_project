# DOCKER_VERSION 1.0.1
FROM lexmarkweb/docker-aem-base
MAINTAINER mikemarr

#Copies required build media
ONBUILD ADD cq-publish-4503.jar /aem/cq-publish-4503.jar
ONBUILD ADD license.properties /aem/license.properties
ONBUILD ADD https://raw.githubusercontent.com/LexmarkWeb/docker-aem-publisher/master/postInstallHook.sh /aem/postInstallHook.sh
ONBUILD RUN chmod +x /aem/postInstallHook.sh

#uploads optional packages
ONBUILD ADD *.zip /aem/packages/

#Extracts AEM
ONBUILD WORKDIR /aem
ONBUILD RUN java -XX:MaxPermSize=256m -Xmx1024M -jar cq-publish-4503.jar -unpack -r publish -p 4503

# Installs AEM
ONBUILD RUN ["/aem/aemInstaller.sh","-i","cq-publish-4503.jar","-r","publish","-p","4503"]

ONBUILD WORKDIR /aem/crx-quickstart/bin
#Replaces the port within the quickstart file with the standard publisher port
ONBUILD RUN cp quickstart quickstart.original
ONBUILD RUN cat quickstart.original | sed "s|4502|4503|g" > quickstart

EXPOSE 4503 8000
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
