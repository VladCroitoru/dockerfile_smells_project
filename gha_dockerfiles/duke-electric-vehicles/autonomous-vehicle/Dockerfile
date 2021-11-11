ARG FROM_IMAGE=ros:foxy
ARG OVERLAY_WS=/opt/ros/dev_ws

# multi-stage for caching
FROM $FROM_IMAGE AS cacher

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
ADD ros_packages .

# copy manifests for caching
WORKDIR /opt
RUN mkdir -p /tmp/opt && \
    find ./ -name "package.xml" | \
      xargs cp --parents -t /tmp/opt && \
    find ./ -name "COLCON_IGNORE" | \
      xargs cp --parents -t /tmp/opt || true

# multi-stage for building
FROM $FROM_IMAGE AS builder

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y build-essential net-tools vim wget
RUN apt install -y nano
RUN apt install -y python3-pip
RUN apt install -y ros-foxy-rqt*

RUN pip3 install Cython
RUN pip3 install sbp
RUN pip3 install numpy --upgrade

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
COPY --from=cacher /tmp/$OVERLAY_WS/src ./src
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/ \
      --ignore-src \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
COPY --from=cacher $OVERLAY_WS/src ./src
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --mixin $OVERLAY_MIXINS

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y neovim

RUN pip3 install --upgrade pynvim
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN mkdir -p ~/.config/nvim/autoload
RUN curl -fLO https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
RUN mv plug.vim $HOME/.config/nvim/autoload/plug.vim

RUN mkdir -p ~/.config/nvim
RUN echo "function! s:check_back_space() abort\n\
  let col = col('.') - 1\n\
  return !col || getline('.')[col - 1]  =~ '\s'\n\
endfunction\n\
\n\
inoremap <silent><expr> <Tab>\n\
      \ pumvisible() ? \"\<C-n>\" :\n\
      \ <SID>check_back_space() ? \"\<Tab>\" :\n\
      \ coc#refresh()\n\
\n\
nnoremap <space>w <C-w>\n\
call plug#begin(stdpath('data') . '/plugged')\n\
Plug 'neoclide/coc.nvim', {'branch': 'release'}\n\
Plug 'dracula/vim', { 'as': 'dracula' }\n\
call plug#end()\n\
colorscheme dracula" > $HOME/.config/nvim/init.vim

RUN mkdir $HOME/.config/coc
RUN nvim --headless +PlugInstall +qall
RUN mkdir -p $HOME/.config/coc/extensions
RUN cd $HOME/.config/coc/extensions && npm install coc-pyright --global-style --ignore-scripts --no-bin-links --no-package-lock --only=prod

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh
