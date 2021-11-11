FROM louisdorard/dev-base
MAINTAINER Louis Dorard <louis@dorard.me>

# Install s3cmd to make it easy to dl/ul data to Amazon S3
RUN apt-get install -y s3cmd

# Install "mini" anaconda python distribution (python 2.7) and a couple of packages
WORKDIR /downloads
RUN wget http://repo.continuum.io/miniconda/Miniconda-3.5.2-Linux-x86_64.sh
RUN /bin/bash Miniconda-3.5.2-Linux-x86_64.sh -b -p /work/anaconda/
RUN rm Miniconda-3.5.2-Linux-x86_64.sh
RUN /work/anaconda/bin/conda update conda
RUN /work/anaconda/bin/conda install pandas scikit-learn ipython-notebook --yes
RUN echo "export PATH=\"\$PATH:/work/anaconda/bin\"" >> ~/.zshrc

# IPython notebooks
RUN mkdir -p /ipynb
RUN echo "alias ipynb='ipython notebook --ip=0.0.0.0 /ipynb/'" >> ~/.zshrc
