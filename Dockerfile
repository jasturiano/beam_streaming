FROM python:3.9

ARG WORKDIR=/beam_app
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

ENV PYTHON_REQUIREMENTS_FILE="${WORKDIR}/requirements.txt"
ENV PYTHON_PY_FILE="${WORKDIR}/main.py"

COPY . "/${WORKDIR}"

RUN echo '----- listing workdir'
RUN ls -la ${WORKDIR}

RUN apt-get update \
    && apt-get install -y \
    && pip install --no-cache-dir --upgrade pip \
    && pip install -r requirements.txt


# Define the command to run when the container starts
CMD ["python", "your_pipeline_script.py"]
