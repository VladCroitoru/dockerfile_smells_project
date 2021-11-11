FROM mpender/ansible-docker

RUN useradd armviz

RUN yum install -y epel-release \
		bzip2 \
		gcc

RUN yum install -y npm \

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /tmp

RUN git clone https://github.com/ytechie/AzureResourceVisualizer.git

WORKDIR /tmp/AzureResourceVisualizer/

RUN chmod -R 777 /tmp/AzureResourceVisualizer/

RUN npm install

RUN npm install -g gulp bower typings typescript

# Bower needs non-root user
USER armviz

WORKDIR /tmp/AzureResourceVisualizer/

RUN bower install

USER root

RUN typings install

EXPOSE 3000 3001

CMD ["gulp", "serve"]
