# docker image to download yum rpms via dependencies
# these are the centos tags you can use below if you want to use a different version of centos
#latest, centos7, 7 (docker/Dockerfile)
#centos6, 6 (docker/Dockerfile)
#centos5, 5 (docker/Dockerfile)
#centos7.1.1503, 7.1.1503 (docker/Dockerfile)
#centos7.0.1406, 7.0.1406 (docker/Dockerfile)
#centos6.7, 6.7 (docker/Dockerfile)
#centos6.6, 6.6 (docker/Dockerfile)
#centos5.11, 5.11 (docker/Dockerfile)

FROM centos:latest
MAINTAINER "Jeremy Brown" <jeremy@tenfourty.com>
ENV container docker

# install yum-utils for the yumdownloader command and epel for additional epel packages
# if you needed additional repositories you could do that here
RUN yum install -y yum-utils epel-release

# create my rpms directory (mount your local volume to this path)
RUN mkdir /rpms

# effectively we are running this command
# yumdownloader --destdir=/rpms/ --resolve ansible git curl
# CMD contains the defaults but you can override these by providing different arguments - see README.md for examples

ENTRYPOINT ["yumdownloader", "--destdir=/rpms/", "--resolve"]
CMD ["ansible","git","curl"]
