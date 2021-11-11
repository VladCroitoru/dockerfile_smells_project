FROM continuumio/miniconda3
EXPOSE 80
RUN apt-get update -y && apt-get install -y nginx supervisor vim
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN conda install -y \
        flask \
        pillow \
        numpy \
        scipy \
        pandas \
        scikit-learn && \
    pip install flask_bootstrap flask_wtf gunicorn && \
    conda install -y -c conda-forge bokeh phantomjs selenium
COPY etc/nginx.conf /etc/nginx/sites-available/default
COPY etc/supervisor.conf /etc/supervisor/conf.d/app.conf
ADD . /app
ENV PYTHONPATH /app
# this is to prevent an error where phantomjs crashes
ENV OPENSSL_CONF $WORKSPACE/openssl.cnf
CMD ["/usr/bin/supervisord","-n"]
