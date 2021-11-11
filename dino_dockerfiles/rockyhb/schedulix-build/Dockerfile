FROM rockyhb/schedulix-requirements
MAINTAINER Claas Rockmann-Buchterkirche <claas@rockbu.de>
WORKDIR /tmp
RUN ls -laF
RUN cp swt.jar /usr/share/java/
RUN useradd schedulix
RUN su schedulix -c "cd /home/schedulix && git clone https://github.com/schedulix/schedulix.git -b v2.6.1 schedulix-2.6.1"
ADD bashrc /home/schedulix/.bashrc
RUN su - schedulix -c "cd /home/schedulix/schedulix-2.6.1/src && make && cd /home/schedulix && tar czf schedulix-2.6.1.tgz schedulix-2.6.1"
RUN echo Done.
CMD /bin/bash
