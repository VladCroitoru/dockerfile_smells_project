FROM centos:7

RUN yum install -y -q epel-release && \
    yum install -y -q python-pip && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    pip install https://github.com/openmicroscopy/zeroc-ice-py-centos7/releases/download/0.0.3/zeroc_ice-3.6.4-cp27-cp27mu-linux_x86_64.whl

RUN pip install omego && \
    mkdir -p /opt/omero && \
    cd /opt/omero && \
    omego download python --sym OMERO.py && \
    echo /opt/omero/OMERO.py/lib/python > /usr/lib/python2.7/site-packages/omero.pth

COPY *.py /opt/omero-prometheus-tools/
COPY omero_prometheus_tools /opt/omero-prometheus-tools/omero_prometheus_tools/
COPY etc /opt/omero-prometheus-tools/etc/
RUN cd /opt/omero-prometheus-tools/ && \
    python setup.py install
ENTRYPOINT ["/usr/bin/omero-prometheus-tools.py"]
