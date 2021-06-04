FROM python:3.9

ARG ARG_VAR

ENV ENV_VAR_DOCKERFILE="variavel_de_ambiente_Dockerfile"
ENV ENV_ARG=${ARG_VAR}

WORKDIR /code

COPY . /code

RUN pip install numpy

CMD python cod_python.py