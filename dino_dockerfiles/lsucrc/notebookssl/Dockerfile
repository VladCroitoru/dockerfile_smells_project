#Version 1.1
#add the base image
FROM lsucrc/crcbase
RUN  yum install -y python-pip python-devel sqlite3 libpng-devel freetype-devel openssl netcdf-devel
RUN  pip install jupyter matplotlib netCDF4

# Add a notebook profile.
RUN mkdir -p -m 700 /root/.jupyter/custom && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.tornado_settings = { 'headers': { 'Content-Security-Policy': \"frame-ancestors * \" } }" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "define(['base/js/namespace'], function(Jupyter){ Jupyter._target = '_self'; });" >> /root/.jupyter/custom/custom.js 

VOLUME /notebooks
WORKDIR /notebooks

# Add Tini. Tini operates as a process subreaper for jupyter to prevent crashes.
ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

# Generate the private key and certificate
RUN openssl genrsa -out /etc/ssl/certs/server.key 2048 && \
    openssl req -new -x509 -key /etc/ssl/certs/server.key -out /etc/ssl/certs/server.csr -days 3650 -subj /CN=localhost && \
    echo "c.NotebookApp.certfile = '/etc/ssl/certs/server.csr'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.keyfile = '/etc/ssl/certs/server.key'" >> /root/.jupyter/jupyter_notebook_config.py 

ENTRYPOINT ["/usr/bin/tini", "--"]

# Run jupyter
EXPOSE 9999
CMD ["jupyter", "notebook", "--port=9999", "--no-browser", "--ip=0.0.0.0"]
