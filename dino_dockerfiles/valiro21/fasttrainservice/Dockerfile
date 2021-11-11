FROM valiro21/fasttrainservice-build-environment:latest
MAINTAINER Valentin Rosca<rosca.valentin2012@gmail.com>
COPY ./ /FastTrainService
RUN cd /FastTrainService && cmake -DCMAKE_BUILD_TYPE=RELEASE -DDOCKER_RELEASE=1 ./ && make
RUN cp /FastTrainService/Server/bin/RELEASE/FastTrainServer ./
EXPOSE 8181
CMD ["/FastTrainServer"]