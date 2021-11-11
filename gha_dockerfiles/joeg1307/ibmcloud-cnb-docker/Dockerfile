FROM ubuntu:21.10
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 
ENV LANG en_US.utf8
ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
RUN apt-get update && apt-get -y install curl && apt-get -y install git && \
     apt-get -y install vim  && \
     apt-get -y install nodejs && apt-get -y install npm &&\  
     apt-get -y install openjdk-8-jdk && \ 
     apt-get -y install wget && \ 
     echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> .bashrc && echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bashrc
RUN curl -sL https://raw.githubusercontent.com/IBM-Cloud/ibm-cloud-developer-tools/master/linux-installer/idt-installer | bash
RUN echo '[[ -f /usr/local/ibmcloud/autocomplete/bash_autocomplete ]] && source /usr/local/ibmcloud/autocomplete/bash_autocomplete' >> .bashrc
RUN echo 'alias ic="ibmcloud"' >> .bashrc 
RUN echo 'alias l="ls -l"' >> .bashrc
RUN wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/4.8.13/openshift-client-linux-4.8.13.tar.gz && tar -xvf openshift-client-linux-4.8.13.tar.gz && mv oc /usr/local/bin/
RUN . ~/.bashrc
WORKDIR /bootcamp
RUN git clone https://github.com/IBM/container-service-getting-started-wt.git && \
    git clone https://github.com/ibm-cloud-academy/LightBlueCompute && \
    curl https://bootcamp-gradle-build.mybluemix.net/ms/catalog --output catalog.jar && \
    curl https://bootcamp-gradle-build.mybluemix.net/ms/customer --output customer.jar
CMD ["bash"]
VOLUME [ "/bootcamp" ]