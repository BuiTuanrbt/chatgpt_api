FROM conda/miniconda3

RUN apt-get update

RUN apt-get -y install ffmpeg libglib2.0-0 libsm6 libxext6 libxrender-dev gcc python3-dev python3-numpy libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libgtk-3-dev libgtk-3-dev libgtk2.0-dev

RUN conda create -n sample python=3.8.3

ENV PATH /opt/conda/envs/sample/bin:$PATH

RUN /bin/bash -c "source activate sample"

RUN conda install python=3.8.3
RUN /bin/bash -c "pip install cmake"
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install basicsr
RUN pip install --upgrade pip setuptools wheel
RUN pip install setuptools==58.2.0

EXPOSE 10014

COPY . .
WORKDIR /app/GFPGAN
RUN python setup.py develop
WORKDIR /app
RUN pip install pydantic[dotenv]
CMD ["uvicorn", "manage:app", "--host","0.0.0.0", "--port","10014"]