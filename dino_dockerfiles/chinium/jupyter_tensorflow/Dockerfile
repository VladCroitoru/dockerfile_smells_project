FROM centos:7
MAINTAINER Myeongjo Jin
RUN yum -y update
RUN yum -y groupinstall "Development Tools"
RUN yum -y install epel-release && \
    yum -y install python-devel python-pip lapack-devel freetype-devel \
           libpng-devel libjpeg-turbo-devel ImageMagick
RUN pip install --upgrade pip
RUN pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.2.0-cp27-none-linux_x86_64.whl
RUN pip install pandas==0.18.1 scipy==0.17.1 && \
    pip install jupyter-core==4.1.0 notebook==4.2.1 jupyter-client==4.3.0 jupyter-console==4.1.1 jupyter==1.0.0 && \
    pip install scikit-learn==0.17.1 matplotlib==1.5.1 Pillow==3.2.0 && \
    pip install google-api-python-client==1.5.1
RUN cd /etc/yum.repos.d && \
    curl -LO http://www.graphviz.org/graphviz-rhel.repo && \
    cd /tmp && \
    curl -LO http://www.graphviz.org/pub/graphviz/stable/redhat/el7Server/x86_64/os/gts-0.7.6-21.20111025.el7.x86_64.rpm && \
    yum -y install graphviz-2.38.0-1.el7 graphviz-gd-2.38.0-1.el7 gts-0.7.6-21.20111025.el7.x86_64.rpm

RUN jupyter notebook --generate-config && \
    ipython profile create
RUN echo "c.NotebookApp.ip = '*'" >>/root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >>/root/.jupyter/jupyter_notebook_config.py && \
    echo "c.InteractiveShellApp.matplotlib = 'inline'" >>/root/.ipython/profile_default/ipython_config.py  
#RUN echo "c.Application.log_level = 'DEBUG'" >>/root/.jupyter/jupyter_notebook_config.py

ADD init.sh /usr/local/bin/init.sh
RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 8888
CMD ["/usr/local/bin/init.sh"]
