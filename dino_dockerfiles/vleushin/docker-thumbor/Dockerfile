FROM apsl/thumbor-multiprocess

RUN \ 
    ln /usr/lib/python2.7/dist-packages/cv2.x86_64-linux-gnu.so /usr/local/lib/python2.7/cv2.so && \
    ln /usr/lib/python2.7/dist-packages/cv.py /usr/local/lib/python2.7/cv.py

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["thumbor"]
