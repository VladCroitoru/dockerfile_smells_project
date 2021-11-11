FROM jupyter/minimal-notebook:latest
MAINTAINER Kacper Kowalik <xarthisius.kk@gmail.com>
RUN pip install -U ytree yt-astro-analysis git+https://github.com/data-exp-lab/yt-canvas-widget
RUN ipython -c 'from matplotlib.font_manager import FontManager; FontManager()'
RUN yt config set yt test_data_dir /home/jovyan/work/data
WORKDIR /home/jovyan/work
