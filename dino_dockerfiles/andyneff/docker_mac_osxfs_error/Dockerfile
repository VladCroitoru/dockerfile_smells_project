FROM centos:7

RUN yum groupinstall -y "Development tools"

RUN useradd dev

ADD http://download.osgeo.org/proj/proj-4.9.1.tar.gz http://download.osgeo.org/proj/proj-datumgrid-1.5.zip proj proj.spec /tmp/

RUN chmod 777 /tmp/proj*

USER dev

CMD /tmp/proj
