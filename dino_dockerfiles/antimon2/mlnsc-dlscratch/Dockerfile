FROM continuumio/miniconda3:4.3.14

MAINTAINER antimon2 <antimon2.me@gmail.com>

# Install NumPy / Matplotlib / Jupyter.
RUN /opt/conda/bin/conda install numpy matplotlib jupyter -y --quiet

# Install libzmq
RUN apt-get update \
    && apt-get upgrade -y -o Dpkg::Options::="--force-confdef" -o DPkg::Options::="--force-confold" \
    && apt-get install -y \
    libzmq3-dev \
    libzmq3

# Install Julia0.6.0
RUN mkdir -p /opt/julia-0.6.0 && \
    curl -s -L https://julialang.s3.amazonaws.com/bin/linux/x64/0.6/julia-0.6.0-linux-x86_64.tar.gz | tar -C /opt/julia-0.6.0 -x -z --strip-components=1 -f -
RUN ln -fs /opt/julia-0.6.0 /opt/julia-0.6

# Make v0.6.0 default julia
RUN ln -fs /opt/julia-0.6.0 /opt/julia

# RUN echo "PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt/julia/bin\"" > /etc/environment && \
#     echo "export PATH" >> /etc/environment && \
#     echo "source /etc/environment" >> /root/.bashrc

ENV PATH /opt/julia/bin:$PATH

# Install IJulia with using installed miniconda, and then precompile it
RUN CONDA_JL_HOME=/opt/conda /opt/julia/bin/julia -e 'Pkg.add("IJulia");Pkg.build("IJulia");using IJulia'

# Install PyPlot with using installed matplotlib, and then precompile it
RUN PYTHON=/opt/conda/bin/python /opt/julia/bin/julia -e 'Pkg.add("PyPlot");using PyPlot'

# v0.3: add_iruby: install requirements
RUN apt-get install -y \
    gawk g++ gcc libssl-dev make libc6-dev zlib1g-dev libyaml-dev libsqlite3-dev sqlite3 \
    autoconf libgmp-dev libgdbm-dev libncurses5-dev automake libtool bison pkg-config \
    libffi-dev libgmp-dev libreadline6-dev 

# v0.4: add_iruby: install ruby-2.4.1
RUN cd ~ && curl -o ruby-2.4.1.tar.gz http://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz && \
    tar zxvf ruby-2.4.1.tar.gz && \
    cd ruby-2.4.1 && \
    ./configure --prefix=/usr/local --disable-install-doc && \
    make && make install && \
    cd ~ && rm -rf ruby-2.4.1

# v0.3: add_iruby: install iruby
RUN gem install cztop --no-rdoc --no-ri
RUN cd ~ && git clone https://github.com/zeromq/czmq && \
    cd czmq && \
    ./autogen.sh && ./configure && make && make install && \
    cd ~ && rm -rf czmq
RUN gem install iruby --no-rdoc --no-ri
RUN IPYTHONDIR=/opt/conda/share/jupyter iruby register --force

# v0.3: add_iruby: install related library and gems
RUN apt-get install -y gnuplot && \
    gem install pry pry-doc numo-narray numo-gnuplot --no-rdoc --no-ri

# Define working directory.
WORKDIR /opt/notebooks

# EXPOSE
EXPOSE 8888

# Define default command.
# CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser"]
CMD ["/bin/bash"]
