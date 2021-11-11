FROM rpmbuild/centos7

USER root
RUN sed -i -e 's/Defaults    requiretty.*/ #Defaults    requiretty/g' /etc/sudoers

USER builder
CMD /bin/bash
