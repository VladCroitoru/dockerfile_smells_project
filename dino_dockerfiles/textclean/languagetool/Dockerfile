FROM frolvlad/alpine-oraclejdk8:slim
MAINTAINER nickg
WORKDIR /tmp
ADD https://languagetool.org/download/LanguageTool-3.7.zip /tmp/LanguageTool-3.7.zip
RUN /bin/true \
  && apk update && apk upgrade \
  && apk add zip \
  && unzip /tmp/LanguageTool-3.7.zip \
  && mv /tmp/LanguageTool-3.7 /usr/languagetool \
  && rm /tmp/* \
  && apk del zip \
  && rm -rf /var/cache/apk/*
# Too many useful tools to limit to one
#ENTRYPOINT [ "java", "-jar", "/usr/languagetool/languagetool-commandline.jar" ]

