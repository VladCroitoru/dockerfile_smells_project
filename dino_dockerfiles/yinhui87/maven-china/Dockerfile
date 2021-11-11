FROM maven

MAINTAINER Kuiki 911yinhui911@163.com

RUN sed -Ee "s/(<mirrors>)/\1\n    <mirror>\n      <id>alimaven<\/id>\n      <mirrorOf>central<\/mirrorOf>\n      <name>aliyun maven<\/name>\n      <url>http:\/\/maven.aliyun.com\/nexus\/content\/groups\/public\/<\/url>\n    <\/mirror>/" -i /usr/share/maven/conf/settings.xml
