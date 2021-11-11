FROM quay.io/pypa/manylinux1_x86_64

RUN cd; wget https://pypi.python.org/packages/source/p/python-libsbml/python_libsbml-5.13.0.tar.gz --no-check-certificate; tar xf python_libsbml-5.13.0.tar.gz
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp35-cp35m/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp35-cp35m-linux_x86_64.whl
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp34-cp34m/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp34-cp34m-linux_x86_64.whl
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp33-cp33m/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp33-cp33m-linux_x86_64.whl
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp27-cp27mu/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp27-cp27mu-linux_x86_64.whl
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp27-cp27m/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp27-cp27m-linux_x86_64.whl
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp26-cp26mu/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp26-cp26mu-linux_x86_64.whl
RUN cd /root/python-libsbml-5.13.0; /opt/python/cp26-cp26m/bin/python setup.py bdist_wheel; auditwheel repair dist/python_libsbml-5.13.0-cp26-cp26m-linux_x86_64.whl
