# DOCKER-VERSION 1.0.1
FROM lexmarkweb/docker-aem-base
MAINTAINER mikemarr 

#Copies required build media
ONBUILD ADD cq-author-4502.jar /aem/cq-author-4502.jar
ONBUILD ADD license.properties /aem/license.properties
ONBUILD ADD https://raw.githubusercontent.com/LexmarkWeb/docker-aem-author/master/postInstallHook.sh /aem/postInstallHook.sh
ONBUILD RUN chmod +x /aem/postInstallHook.sh

#uploads optional packages
ONBUILD ADD *.zip /aem/packages/

# Extracts AEM
ONBUILD WORKDIR /aem
ONBUILD RUN java -XX:MaxPermSize=256m -Xmx1024M -jar cq-author-4502.jar -unpack -r nosamplecontent


# Installs AEM
ONBUILD RUN ["/aem/aemInstaller.sh","-i","cq-author-4502.jar","-r","author","-p","4502"]

EXPOSE 4502 8000
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
