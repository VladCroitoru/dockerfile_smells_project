FROM python:3.6

# Use python script to get all dependencies of texlive-full, then filter
# out the *-doc ones and install. Finally, clean up temporary files.
COPY install_tex.py /
RUN apt-get update && python /install_tex.py &&\
    apt-get clean &&\
    apt-get autoclean -y &&\
    apt-get autoremove -y &&\
    apt-get clean &&\
    rm -rf /tmp/* /var/tmp/* &&\
    rm -rf /var/lib/apt/lists/*

CMD python --version
