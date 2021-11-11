FROM centos:7.3.1611
RUN yum -y install epel-release; yum clean all
RUN yum -y group install "Development Tools"
RUN yum -y install install python-devel
RUN yum -y install python-pip; yum clean all && pip install --upgrade pip numpy scipy pandas scikit-learn matplotlib seaborn tensorflow keras jupyter jupyter_contrib_nbextensions
COPY jupyter_notebook_config.json /root/.jupyter/
