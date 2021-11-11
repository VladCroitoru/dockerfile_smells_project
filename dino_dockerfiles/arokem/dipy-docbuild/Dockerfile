FROM arokem/dipy
MAINTAINER Ariel Rokem <arokem@gmail.com>
# Install all the optional dependencies (sklearn, cvxopt, vtk):
RUN apt-get update && apt-get install -y git \
Xvfb \
python-vtk \
texlive-latex-recommended \
texlive-latex-extra \
texlive-fonts-recommended
RUN pip install cython
RUN pip install sphinx
RUN pip install xvfbwrapper
ENV TEST_WITH_XVFB=true
CMD git clone https://github.com/nipy/dipy.git && cd dipy && git checkout maint/0.10.x && python setup.py install && cd doc && make upload
