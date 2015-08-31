# flask-blueprints-boilerplate

## Development

### Spinning Up Mongo Container

```
docker-machine create --driver virtualbox dev
docker-machine env dev
eval "$(docker-machine env dev)"
docker-machine ip dev

docker run -p 27017:27017 --name mongo_001 -d mongo
```

### Populating Mongo
```
scripts/postcompose_init.sh
```

Update the `MONGODB_HOST` in `config.py` to use the `dev` machine's ip address.
Make sure `run.py` is instantiated for development with the following line: `app = create_app('DEVELOPMENT')`

### Running the Server

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Running the Integration Tests

```
cd tests
nosetests -v .
```

### Running the Selenium Tests
