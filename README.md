# RESTFUL service


## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# get the image 
docker pull aboshchenko/flask-restapi:latest
# run the image 
docker run aboshchenko/flask-restapi:latest
```

## Testing
Test are located in the /test/test_default_controller.py file.
