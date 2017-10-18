# Sharding

I made a small little script that will take a large folder (possibly a large image or file directory) and breaks it into smaller
folders using the first 3 letters of the filename.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

A step by step series of examples that tell you have to get a development env running

Clone the repository

```
git clone https://github.com/JamesSingleton/Sharding.git
```

Open the folder up in a text editor of your choice

You can change the source and dest file locations to your choosing. This project is setup to use the directory and folders provided.

```
baseDirectory = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

source = baseDirectory+'/Shard_Source/'

dest = baseDirectory+'/Shard_Dest/'
```


## Running the tests

Lets get to sharding some folders and files

### Break down into end to end tests

Open up your command prompt and cd into this directory

```
cd path/path/sharding
```

Run the shard.py script

```
python shard.py
```

## Built With

* [Python](https://www.python.org/downloads/)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/JamesSingleton/Sharding/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **James Singleton** - *Initial work* - [JamesSingleton](https://github.com/JamesSingleton)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
