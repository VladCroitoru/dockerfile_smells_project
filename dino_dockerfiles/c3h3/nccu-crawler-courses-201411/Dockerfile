FROM c3h3/oblas-py278-shogun

EXPOSE 8888
ENV IPYNB_PROFILE "c3h3-dark"
#ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib

RUN mkdir demo_ipynbs
ADD 20141129LiveDemo.ipynb /demo_ipynbs/20141129LiveDemo.ipynb 
ADD 20141130LiveDemo.ipynb /demo_ipynbs/20141130LiveDemo.ipynb

WORKDIR demo_ipynbs

RUN pip install networkx html5lib BeautifulSoup4
RUN ipython profile create c3h3-dark

ADD c3h3_custom.css /root/.ipython/profile_c3h3-dark/static/custom/custom.css
COPY ipython_notebook_config.py /root/.ipython/profile_c3h3-dark/ipython_notebook_config.py 
COPY ipython_notebook_config.py /root/.ipython/profile_default/ipython_notebook_config.py
CMD ipython notebook --no-browser --ip=0.0.0.0 --port 8888 --profile=$IPYNB_PROFILE

