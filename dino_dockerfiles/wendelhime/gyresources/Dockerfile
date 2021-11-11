FROM wendelhime/basic:latest

RUN apt-get update && \
        apt-get install -y postgresql \
        openjdk-8-jdk \
        apt-transport-https \
        wget

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list
RUN wget -O - 'https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc' | apt-key add -
RUN echo "deb https://dl.bintray.com/rabbitmq/debian stretch main" | tee -a /etc/apt/sources.list.d/bintray.rabbitmq.list
RUN echo "deb http://dl.bintray.com/rabbitmq/debian stretch erlang" >> /etc/apt/sources.list.d/bintray.rabbitmq.list


RUN apt update && apt install -y elasticsearch erlang-nox rabbitmq-server

WORKDIR /root/git
RUN git clone https://github.com/CapivaraProjects/GYResources && \
        pip3 install -r GYResources/requirements.txt
WORKDIR /root/git/GYResources
RUN git submodule update --init --recursive && \
        git submodule foreach git pull origin master && \
        export PYTHONPATH=$PYTHONPATH:/root/git/GYResources

# ENTRYPOINT ["/usr/bin/zsh", "-c", "./execute.sh"]
