FROM java:8
LABEL maintainer "Lars Tiedemann Thorsen <lars.thorsen@evry.com>"
ENV READYAPI_VERSION=2.5.0 READYAPI_LICENSE_MANAGER_VERSION=1.2.5 LICENSE_SERVER=fslicense.evry.com:1099

ADD run-readyAPI.sh run-readyAPI.sh

RUN apt-get update && apt-get install -y openjfx wget && \
	wget http://dl.eviware.com/ready-api/${READYAPI_VERSION}/ReadyAPI-${READYAPI_VERSION}-linux-bin.tar.gz && \
	tar xvzf ReadyAPI-${READYAPI_VERSION}-linux-bin.tar.gz && rm -rf ReadyAPI-${READYAPI_VERSION}-linux-bin.tar.gz && \
	mv /ReadyAPI-${READYAPI_VERSION} /ReadyAPI && chmod -R 755 /ReadyAPI/bin/ && \
	wget http://dl.eviware.com/ready-api/license-manager/ready-api-license-manager.zip -O ready-api-license-manager.zip && \
	unzip ready-api-license-manager.zip && rm -rf ready-api-license-manager.zip && \
	mv ready-api-license-manager/ready-api-license-manager-${READYAPI_LICENSE_MANAGER_VERSION}.jar ready-api-license-manager.jar && \
	chmod 755 /run-readyAPI.sh

CMD ./run-readyAPI.sh
