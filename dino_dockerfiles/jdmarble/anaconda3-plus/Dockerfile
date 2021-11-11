FROM continuumio/anaconda3:4.3.1

# Install Git LFS support
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install git-lfs && \
    git lfs install

# Install build tools. Don't install runtime dependencies here if you only want to depend on Anaconda!
RUN pip install coverage flake8
