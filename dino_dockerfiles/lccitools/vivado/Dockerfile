# The MIT License
#
#  Copyright (c) 2017, Oleg Nenashev, Stefan Wallentowitz
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM lccitools/base:latest
LABEL Maintainer  Stefan Wallentowitz <stefan@wallentowitz.de>
LABEL Description "Xilinx Vivado"

ARG VERSION=2016.4

VOLUME /tmpfiles
WORKDIR /tmp

ENV VERSION=${VERSION}
ENV VIVADO_BASE=/tools/eda/xilinx
ENV VIVADO_MODULEFILES=/tools/modulefiles/eda/xilinx/vivado

COPY install.sh /tmp/
COPY webpack_config.txt /tmp/

ENTRYPOINT ["./install.sh"]
