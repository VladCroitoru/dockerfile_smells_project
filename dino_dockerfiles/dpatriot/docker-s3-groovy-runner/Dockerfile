FROM dpatriot/docker-s3-runner:1.4.0
MAINTAINER Shago Vyacheslav <v.shago@corpwebgames.com>

RUN curl -s get.sdkman.io | bash \
    && echo "gvm_auto_answer=true" >> ~/.sdkman/etc/config \
    && /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install groovy" \
    && mkdir -p $HOME/.groovy/lib

RUN /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh \
	&& grape install 'com.amazonaws' 'aws-java-sdk' '1.10.40' \
	&& grape install 'mysql' 'mysql-connector-java' '5.1.38'"

#load non-grape libs
RUN curl -o $HOME/.groovy/lib/RedshiftJDBC41-1.1.10.1010.jar https://s3.amazonaws.com/redshift-downloads/drivers/RedshiftJDBC41-1.1.10.1010.jar

#unload lib
RUN rm -f /root/.sdkman/candidates/groovy/current/lib/servlet-api-2.4.jar

ENV GROOVY_HOME /root/.sdkman/candidates/groovy/current
ENV PATH $GROOVY_HOME/bin:$PATH
