FROM murata99/docker-statistics-image

RUN apt-get update && \
    apt-get -y install python-pip && \
    apt-get -y install ipython ipython-notebook && \
    apt-get -y install hdf5-tools && \
    apt-get -y install build-essential libzmq3-dev && \
    pip install --upgrade pip && \
    pip install jupyter

RUN R -q -e "install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), repos='https://cran.ism.ac.jp/'); devtools::install_github('IRkernel/IRkernel'); IRkernel::installspec()"
RUN julia -e 'Pkg.add("IJulia")'

EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
