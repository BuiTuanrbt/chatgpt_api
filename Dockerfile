FROM conda/miniconda3

RUN apt-get update

RUN apt-get -y install ffmpeg libglib2.0-0 libsm6 libxext6 libxrender-dev gcc python3-dev python3-numpy libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libgtk-3-dev libgtk-3-dev libgtk2.0-dev

RUN conda create -n sample python=3.6

ENV PATH /opt/conda/envs/sample/bin:$PATH

RUN /bin/bash -c "source activate sample"

RUN conda install python=3.6

RUN /bin/bash -c "pip install matplotlib>=3.2.2"
RUN /bin/bash -c "pip install numpy>=1.18.5"
RUN /bin/bash -c "pip install opencv-python>=4.1.1"
RUN /bin/bash -c "pip install Pillow>=7.1.2"
RUN /bin/bash -c "pip install PyYAML>=5.3.1"
RUN /bin/bash -c "pip install requests>=2.23.0"
RUN /bin/bash -c "pip install scipy>=1.4.1"
RUN /bin/bash -c "pip install torch>=1.7.0,!=1.12.0"
RUN /bin/bash -c "pip install torchvision>=0.8.1,!=0.13.0"
RUN /bin/bash -c "pip install tqdm>=4.41.0"
RUN /bin/bash -c "pip install protobuf<4.21.3"
RUN /bin/bash -C "pip install tensorboard>=2.4.1"
RUN /bin/bash -C "pip install ipython"
RUN /bin/bash -C "pip install psutil"
RUN /bin/bash -C "pip install thop"
RUN /bin/bash -C "pip install pandas>=1.1.4"
RUN /bin/bash -C "pip install seaborn>=0.11.0"


EXPOSE 8092

COPY . .
CMD ["uvicorn", "manage:app", "--host","0.0.0.0", "--port","8092"]