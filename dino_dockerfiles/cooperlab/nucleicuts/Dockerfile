FROM dsarchive/histomicstk:latest
MAINTAINER Lee Cooper <lee.cooper@emory.edu>

#install requirements of pygco
RUN cd / && \
    git clone https://github.com/yujiali/pygco.git && \
    cd pygco && \
    make

ENV PYTHONPATH=/pygco/pygco   

# Copy plugin files and install any requirements
ENV my_plugin_path=$htk_path/../my_plugin
RUN mkdir -p $my_plugin_path
COPY . $my_plugin_path
RUN cd $my_plugin_path && \
    conda install --yes --file requirements.txt --file requirements_c_conda.txt && \
    pip install -r requirements.txt && \
    pip install -r requirements_c.txt && \
    pip install -e . 
    
# use entrypoint provided by slicer_cli_web
WORKDIR $my_plugin_path/Applications
ENTRYPOINT ["/build/miniconda/bin/python" ,"/build/slicer_cli_web/server/cli_list_entrypoint.py"] 
