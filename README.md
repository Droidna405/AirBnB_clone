# Welcome to an AirBnB Clone (ALX B&B)

![Air_BnB_clone logo](img/air_bnb_clone.png)

---
# Overview
AirBnB Clone is a command-line interface (CLI) program designed to manage class instances within the AirBnB project. It provides functionalities to create, update, delete, and display instances of various classes.

## Getting Started
To begin using the CLI, follow these steps:

```bash
Clone the repo and start the console:
==========================================

git clone https://github.com/Droidna405/AirBnB_clone.git
cd AirBnB_clone
./console.py
```

---
## Usage
Once the console is running, you can explore its functionalities:

    Type help to see a list of available commands and their usage.
    Use commands like create, destroy, show, update, etc., followed by the class name to interact with specific class instances.
    For detailed usage instructions for a specific command, type help <command>.

## Usage and Examples

```bash
./console.py

# Create a BaseModel instance and print its id
(anb) create BaseModel
b61e46d6-9143-4d37-b271-ce76a759d6a6

# to print the instance
(anb) show BaseModel b61e46d6-9143-4d37-b271-ce76a759d6a6
[BaseModel] (b61e46d6-9143-4d37-b271-ce76a759d6a6) {'id': 'b61e46d6-9143-4d37-b271-ce76a759d6a6', 'created_at': datetime.datetime(2021, 6, 30, 11, 34, 53, 117968), 'updated_at': datetime.datetime(2021, 6, 30, 14, 34, 53, 118060)}

# to print all object created previously
(anb) all
["[BaseModel] (b61e46d6-9143-4d37-b271-ce76a759d6a6) {'id': 'b61e46d6-9143-4d37-b271-ce76a759d6a6', 'created_at': datetime.datetime(2021, 6, 30, 11, 34, 53, 117968), 'updated_at': datetime.datetime(2021, 6, 30, 14, 34, 53, 118060)}", "[BaseModel] (426aea0f-5012-4a52-9a3a-3c775ff98e07) {'id': '426aea0f-5012-4a52-9a3a-3c775ff98e07', 'created_at': datetime.datetime(2021, 6, 30, 13, 29, 6, 1369), 'updated_at': datetime.datetime(2021, 6, 30, 13, 29, 6, 1383)}"]
```

---
## Contributing
Pull requests are welcome.

Please make sure to update tests as appropriate.

---
## License
This software is open-source.

---
## Authors

- Joel Mwangala <joemwangala@gmail.com>
- Michael Ogunnaike <email@here.com>