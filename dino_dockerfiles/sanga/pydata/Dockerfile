from python:3.5.1
maintainer tim@sampson.fi

run echo deb http://llvm.org/apt/jessie/ llvm-toolchain-jessie-3.7 main >> /etc/apt/sources.list
run wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|apt-key add -
run apt-get update
run apt-get install -y wget liblapack-dev fortran-compiler llvm-3.7-dev libedit-dev
workdir /opt  # you can't pip install for the filesystem root
run pip install --upgrade pip
env LLVM_CONFIG=/usr/lib/llvm-3.7/bin/llvm-config
run pip install --egg git+git://github.com/numba/llvmlite@v0.11.0
run pip install numpy
run pip install numba==0.26
run pip install notebook
run pip install ipywidgets
run pip install scipy
run pip install matplotlib
run pip install seaborn
run pip install pandas
run pip install bokeh
run pip install geojson
run pip install folium
run pip install numexpr
run pip install line-profiler

# Install Tini
run curl -L https://github.com/krallin/tini/releases/download/v0.9.0/tini > tini && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

run mkdir /var/notebooks
workdir /var/notebooks

expose 8888

entrypoint ["tini", "--"]
cmd ["jupyter-notebook", "--ip='*'", "--no-browser"]
