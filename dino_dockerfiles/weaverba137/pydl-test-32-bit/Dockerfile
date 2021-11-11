FROM ioft/i386-ubuntu:trusty
MAINTAINER Benjamin Alan Weaver <baweaver@lbl.gov>
#
# Variables.
#
ENV testuser travis
ENV branch master
ENV package weaverba137/pydl
#
# Add a non-privileged user.
#
RUN adduser --disabled-password --gecos "" ${testuser}
RUN chown ${testuser}:${testuser} /home/${testuser}
#
# Tools needed
#
RUN apt-get update && apt-get -y install git # graphviz texlive-latex-extra dvipng
#
# Install miniconda file.
#
COPY Miniconda-latest-Linux-x86.sh /home/${testuser}
RUN chmod a+x /home/${testuser}/Miniconda-latest-Linux-x86.sh
#
# Set user.
#
USER ${testuser}
WORKDIR /home/${testuser}
#
# Conda setup.
#
RUN linux32 -- /bin/bash Miniconda-latest-Linux-x86.sh -b -p ${HOME}/miniconda
ENV PATH=/home/${testuser}/miniconda/bin:${PATH}
RUN conda config --set always_yes yes --set changeps1 no
# RUN conda create -q -n test python=2.7
# RUN source activeate test
RUN conda install -q pytest pip astropy scipy
#
# Clone.
#
RUN git clone --depth=50 --branch=${branch} https://github.com/${package}.git ${package}
WORKDIR /home/${testuser}/${package}
RUN git submodule update --init --recursive
#
# Run test.
#
ENTRYPOINT ["linux32", "--"]
CMD ["python", "setup.py", "test", "-v", "-V"]
