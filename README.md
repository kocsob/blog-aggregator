# blog-aggregator
Balabit coding task

# Using with Docker

## Build

    cd blog-aggregator
    docker build -t blog-aggregator .

## Run
    
    docker run -d /path/to/data_dir:/data blog-aggregator

# Using without Docker

## Install

    apt-get update
    apt-get install -y python2.7 python-pip
    
    cd blog-aggregator
    pip install -r requirements.txt

## Run
    
    python __main__.py --input=/path/to/input.html --output=/path/to/output.json [--log-level=DEBUG]
