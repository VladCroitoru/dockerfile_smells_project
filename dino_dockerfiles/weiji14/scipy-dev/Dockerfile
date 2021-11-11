FROM debian:testing-slim
MAINTAINER Wei Ji Leong <weiji@e-spatial.co.nz>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    # Install python, pip, git
    python \
    python-dev \
    python-pip \
    git \
    
    # Install packages needed to compile scipy from source
    gcc \
    g++ \
    gfortran \
    libblas-dev \
    liblapack-dev \
    cython \
    
    # Fix InsecurePlatformWarning http://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning
    libffi-dev \
    libssl-dev \
    
    # Install setuptools, numpy and scipy from pip
    && pip install --no-cache-dir setuptools numpy scipy \
    
    # Build latest scipy from git (currently 0.19)
    && pip install --no-cache-dir git+https://github.com/scipy/scipy.git \
    
    # Remove compiler and miscellaneous development packages
    && apt-get remove -y \
    python-dev python-pip git gcc g++ gfortran libblas-dev liblapack-dev cython libffi-dev libssl-dev \
    
    # Penultimate purge
    && apt-get autoremove -y \
    
    # Reinstall some scipy needed libraries
    && apt-get install -y --no-install-recommends \
    liblapack3 \
    
    # Cleanup apt cache
    && rm -rf /var/lib/apt/lists/* \

# Initiate python
CMD ["python"]

# Test command (should return (2.23606797749979, 3, 0))
# docker run --rm weiji14/scipy-dev python -c "from scipy.spatial.distance import directed_hausdorff; import numpy as np; u = np.array([(1.0, 0.0),(0.0, 1.0),(-1.0, 0.0),(0.0,-1.0)]); v = np.array([(2.0, 0.0),(0.0, 2.0),(-2.0, 0.0),(0.0, -4.0)]); print directed_hausdorff(u, v);"