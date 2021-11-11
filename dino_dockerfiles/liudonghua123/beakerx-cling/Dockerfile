FROM beakerx/beakerx
MAINTAINER liudonghua123 <liudonghua123@gmail.com>
USER root
# install gcc7
RUN add-apt-repository -y ppa:jonathonf/gcc-7.2
RUN apt-get update -y
RUN apt-get install -y gcc-7
# create gcc alias to gcc-7
RUN cd /usr/bin && ln -s gcc-7 gcc
SHELL ["/bin/bash" ,"-c"]
RUN echo $SHELL
RUN ls -la /bin/
RUN source activate beakerx
# install cling and cling kernel
RUN  mkdir /cling                                   && \
     cd /cling                                      && \
     apt-get update                                 && \
     apt-get install -y cmake                       && \
     apt-get install -y libxml2-dev                 && \
     git clone http://root.cern.ch/git/llvm.git src && \
     cd src                                         && \
     git checkout cling-patches                     && \
     cd tools                                       && \
     git clone http://root.cern.ch/git/cling.git    && \
     git clone http://root.cern.ch/git/clang.git    && \
     cd clang                                       && \
     git checkout cling-patches                     && \
     cd ../../..                                    && \
     mkdir build
RUN apt-get install -y build-essential
RUN cd /cling/build                                       && \
     cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release ../src && \
     cmake --build . -- -j4                         && \
     cmake --build . --target install
RUN ls -l /home
RUN mkdir /home/beakerx/.cache
RUN id
RUN cd /usr/local/share/cling/Jupyter/kernel       && \
     chmod -R 777 /home/beakerx/.cache               && \
     pip install -e .                               && \
     jupyter-kernelspec install cling-cpp17         && \
     jupyter-kernelspec install cling-cpp1z         && \
     jupyter-kernelspec install cling-cpp14         && \
     jupyter-kernelspec install cling-cpp11         && \
     chmod -R 775 /home/beakerx/.cache               && \
     chown -R beakerx.users /home/beakerx/.cache      && \
     rm -rf /cling
#RUN ["/bin/bash", "-c", "source activate beakerx && conda info --envs && conda install xeus-cling notebook -c QuantStack -c conda-forge -y"]
# revert to the default beakerx user
USER beakerx
