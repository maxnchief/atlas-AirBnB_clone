# Atlas-AirBnB Clone

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Command Interpreter](#command-interpreter)
  - [Basic Commands](#basic-commands)

---

## Description
Atlas-AirBnB Clone is a simplified version of the AirBnB web application. The project is part of a larger initiative to replicate the essential backend features of the AirBnB platform, including the creation and management of objects such as users, places, and reviews. The command interpreter is built to interact with the backend storage of the application, manage object serialization to JSON, and enable the dynamic manipulation of models.

The goal of this project is to enhance skills in:
- Python programming
- Object-oriented programming (OOP)
- JSON file handling and persistence
- Creating a command-line interface (CLI)

---

## Features
- Command interpreter to manage the application's data models
- Serialization and deserialization of objects into JSON format
- Persistent storage of objects using JSON files
- CRUD (Create, Read, Update, Delete) operations for multiple classes such as:
  - User
  - State
  - City
  - Place
  - Amenity
  - Review

---

## Technologies Used
- **Python** (v3.x)
- **JSON** (for object storage)
- **Command-line Interface** for interaction with the application
- **OOP Principles**

---

## Usage
To use the command interpreter, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/atlas-AirBnB_clone.git
    cd atlas-AirBnB_clone
    ```

2. Start the command interpreter:
    ```bash
    ./console.py
    ```

3. For help with available commands:
    ```bash
    (hbnb) help
    ```

---

## Command Interpreter

The command interpreter allows the user to create and manage objects, as well as persist them to JSON. Here are some key commands:

### Basic Commands
| Command       | Description                                               |
| ------------- | --------------------------------------------------------- |
| `create <class>` | Creates a new instance of a class and prints its ID     |
| `show <class> <id>` | Displays the string representation of an object     |
| `destroy <class> <id>` | Deletes an object from storage                    |
| `all <class>` | Shows all instances of a class or all objects             |
| `update <class> <id> <attribute_name> <attribute_value>` | Updates an object's attribute |
| `quit` | Exits the command interpreter                                      |
| `EOF` | Exits the command interpreter via `EOF` signal                     |

---
