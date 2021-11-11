FROM quay.io/pypa/manylinux2014_x86_64
RUN mkdir -p /opt/build_dir/jl
WORKDIR /opt/build_dir
COPY setup.py setup.py
COPY setup.cfg setup.cfg
COPY pyproject.toml pyproject.toml 
COPY CMakeLists.txt CMakeLists.txt
COPY c c
COPY jl/PLext.jl jl/PLext.jl
COPY py py
RUN python3.9 -m venv pyenv && source pyenv/bin/activate && python -m pip install numpy pybind11 wheel setuptools auditwheel && yum install wget -y && wget https://julialang-s3.julialang.org/bin/linux/x64/1.6/julia-1.6.3-linux-x86_64.tar.gz && tar xvf ./julia-1.6.3-linux-x86_64.tar.gz && cp ./julia-1.6.3/bin/julia /usr/bin/julia && cp -rf ./julia-1.6.3/lib/* /usr/lib/ && cp -rf ./julia-1.6.3/libexec/* /usr/libexec/ && cp -rf ./julia-1.6.3/share/* /usr/share/ && cp -rf ./julia-1.6.3/include/* /usr/include/
RUN source pyenv/bin/activate && python setup.py bdist_wheel
RUN source pyenv/bin/activate && python -m auditwheel repair --plat manylinux_2_24_x86_64 dist/*.whl