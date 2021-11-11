FROM mtmiller/octave-snapshot

RUN mkdir /code && cd /code && curl https://codeload.github.com/spm/spm12/tar.gz/r7219 | tar -xz && mv spm12-r7219 spm12

RUN cd /code/spm12/src && make PLATFORM=octave && make install PLATFORM=octave && cd ../../..

RUN rm /code/spm12/@file_array/private/file2mat.m

RUN octave --no-window-system --eval "addpath('/code/spm12'); savepath;"