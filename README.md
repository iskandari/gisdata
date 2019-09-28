# geodata
Geospatial data and cluster analysis tutorial


## open source online editor 

http://geojson.io


### Toronto neighborhoods

https://github.com/jasonicarter/toronto-geojson


### Local installation

```bash
# Clone the repo
> git clone https://github.com/luciasantamaria/geodata.git
> cd geodata/tutorial/

# Create a virtual  environment, install virtualenv if needed
> pip install virtualenv
> virtualenv -p python3.4 .env

# Activate virtualenv by sourcing its activation scripts
> source .env/bin/activate
> . .env/bin/activate.fish  # for fish users out there

# Install the project dependencies using pip3.X
> pip3.4 install -r requirements.txt

```

For python2.7 usage, assuming that python is the 2.7 executable: 

```bash
> virtualenv -p python .env2.7
> source .env2.7/bin/activate
> pip install -r requirements2.7.txt

```


### CSV

merge all .csv files in your working directory
```
cat *.csv >merged.csv
```

pretty preint csv in the command line
```
cat data.csv | column -t -s, | less -S
```

### GDAL

```
ogr2ogr -f PostgreSQL PG:"host='localhost' port='5432' dbname='mydb'" data.geojson -nln tablename
```

### Start Jupyter notebook

```bash
jupyter notebook

```

### Start local web server

```bash
python -m SimpleHTTPServer 8000

```
Files will be served at localhost:8000
