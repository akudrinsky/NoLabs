FROM ghcr.io/basedlabs/rfdiffusion:latest

ENV HYDRA_FULL_ERROR=1
ARG rfdiffusion_path=/app/protein_design/RFdiffusion

WORKDIR /app/protein_design
WORKDIR /app
RUN apt-get update
RUN apt-get -y install wget
COPY protein_design/RFdiffusion /app/protein_design/RFdiffusion
RUN mkdir $rfdiffusion_path/models
RUN ls -l $rfdiffusion_path
WORKDIR $rfdiffusion_path/scripts
RUN chmod +x download_models.sh
RUN sed -i 's/\r$//' download_models.sh # Fix line endings to UNIX
RUN ./download_models.sh $rfdiffusion_path/models
WORKDIR /app
ADD . /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
RUN ls -l

ENTRYPOINT ["uvicorn", "protein_design.api:app"]