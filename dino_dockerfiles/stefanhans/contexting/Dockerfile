FROM stefanhans/contexting

MAINTAINER Stefan Hans <stefan.hans@telefonica.com> 

ENV CONTEXTING_HOME /home/Contexting
ENV QT_VERSION_STR 5_5_1

ADD contexting_core/* ${CONTEXTING_HOME}/contexting_core/
ADD unit_testing/test* ${CONTEXTING_HOME}/unit_testing/
ADD unit_testing/ci/* ${CONTEXTING_HOME}/unit_testing/ci/
ADD unit_testing/ci_brick/* ${CONTEXTING_HOME}/unit_testing/ci_brick/

#RUN cd ${CONTEXTING_HOME}/contexting_core && qmake && make
#RUN cd ${CONTEXTING_HOME}/unit_testing/ci && qmake && make
#RUN cd ${CONTEXTING_HOME}/unit_testing/ci_brick && qmake && make
#RUN cd ${CONTEXTING_HOME}/unit_testing && ./testAll

WORKDIR ${CONTEXTING_HOME}

CMD ["/bin/bash"]
