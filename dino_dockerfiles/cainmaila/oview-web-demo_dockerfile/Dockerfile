FROM cainmaila/ubuntu_nvm:yarn
MAINTAINER docker_user cain@cainplay.com
RUN git clone http://60.251.125.207:8888/demo/oview-web-demo.git \ 
	&& cd oview-web-demo \
	&& git checkout origin/demo_2016_1125 \
	&& yarn
WORKDIR /oview-web-demo
EXPOSE 80
CMD ["yarn","start"]
