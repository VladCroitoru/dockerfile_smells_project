FROM centos:7
LABEL maintainer="Mark McKenna <m4rkmckenna@gmail.com>"
RUN yum -y update ; \
	yum install -y ImageMagick ;\
	mkdir -p { /base, /compare, /result }
VOLUME ["/base", "/compare", "/result"]
ADD ["entrypoint.sh", "/entrypoint.sh"]
ENTRYPOINT [ "/entrypoint.sh"]