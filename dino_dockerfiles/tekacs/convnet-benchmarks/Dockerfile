FROM tekacs/thea:latest
# 'docker build --build-arg NAME=$(date +%s)' to rebuild past an ARG line
ARG BENCH=1
RUN	git clone https://github.com/soumith/convnet-benchmarks
ARG REPOS=1
RUN 	git clone https://github.com/lisa-lab/pylearn2 && \
	cd pylearn2 && \
	python setup.py develop
RUN pip install pycuda
RUN	git clone https://github.com/lebedov/scikits.cuda && \
	cd scikits.cuda && \
	python setup.py install

RUN ln -s /usr/local/nvidia/lib64/libcuda.so.1 /root/libcuda.so
ENV LD_LIBRARY_PATH /root:${LD_LIBRARY_PATH}
ENV SKIP legacy
CMD ["python", "convnet-benchmarks/theano/pylearn2_benchmark.py"]
