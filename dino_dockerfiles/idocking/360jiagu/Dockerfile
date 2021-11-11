FROM openjdk:8

ADD jiagu /usr/bin/
ADD sign /usr/bin/

ENV VERSION_SDK_TOOLS "3859397"
ENV DEBIAN_FRONTEND noninteractive
ENV JAR_TIMEOUT="600s"

ENV CONF_UPDATE "0"
ENV CONF_CRASHLOG "0"
ENV CONF_X86 "0"
ENV CONF_MSG "0"
ENV CONF_BUSINESS "0"
ENV CONF_NOCERT "0"

# For chinese user
# RUN sed -i "s/http:\/\/deb\.debian\.org/http:\/\/mirrors\.aliyun\.com/g" /etc/apt/sources.list

RUN apt-get -qq update \
    && apt-get install -qqy --no-install-recommends p7zip-full \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& mkdir 360jiagu \
	&& cd 360jiagu \
	&& wget -q https://down.360safe.com/360Jiagu/360jiagubao_linux_64.zip \
	&& 7z x 360jiagubao_linux_64.zip \
	&& rm 360jiagubao_linux_64.zip \
	&& cd jiagu \
	&& wget -q https://down.360safe.com/360Jiagu/360jiagubao_mac.zip \
	&& unzip -q -o -j 360jiagubao_mac.zip "*/jiagu/jiagu.jar" "*/jiagu/help.txt" -d . \
	&& unzip -q -o -j 360jiagubao_mac.zip "*/jiagu/lib*" -d ./lib \
	&& curl -s https://dl.google.com/android/repository/sdk-tools-linux-${VERSION_SDK_TOOLS}.zip > /sdk.zip \
	&& unzip -q /sdk.zip -d /sdk \
	&& chmod +x ./java/bin/* \
	&& chmod +x /usr/bin/jiagu \
	&& chmod +x /usr/bin/sign \
	&& rm 360jiagubao_mac.zip \
	&& rm /sdk.zip \
	&& cd ../ \
	&& mv ./jiagu / \
	&& rm -rf 360jiagu \
	&& mkdir -p /root/.android \
	&& touch /root/.android/repositories.cfg \
	&& yes | /sdk/tools/bin/sdkmanager --licenses \
	&& /sdk/tools/bin/sdkmanager 'build-tools;27.0.3' \
	&& cp /sdk/build-tools/27.0.3/apksigner /jiagu/java/bin \
	&& cp /sdk/build-tools/27.0.3/lib/apksigner.jar /jiagu/java/bin \
	&& rm -rf /sdk

WORKDIR /jiagu

CMD ["java", "-jar", "/jiagu/jiagu.jar", "-h"]