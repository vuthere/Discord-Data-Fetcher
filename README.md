# Discord User Data Fetcher 🤖

This Python application 🐍 is designed to fetch and save user data from Discord via the Discord API. It provides a simple command-line interface that allows users to interact with their Discord data and perform actions like opening a specific Discord-related URL in the default web browser.

## Features 🌟

- **Fetch User Data** 📥: Retrieves user data including username, avatar, status, and more from Discord.
- **Save Data Locally** 💾: Saves the fetched data in a YAML formatted file with a timestamped filename.

## Technologies Used 💻

This project is built using a variety of modern technologies and libraries to ensure asynchronous operation and seamless interaction with web services. Here are the key technologies and how they contribute to the functionality of the application:

- **Python** 🐍: A powerful, high-level programming language known for its simplicity and readability. It's used here for all backend logic.
- **aiohttp** 🌐: A cutting-edge library for client-side and server-side asynchronous HTTP network communication.
- **Asyncio** ⏳: Python's built-in library for writing concurrent code.
- **Discord API**: Provides a set of programmable interfaces for interacting with Discord data.
- **Docker** 🐳: A platform for developing, shipping, and running applications inside lightweight, portable containers.
- **YAML**: Used for saving the fetched data from Discord in a readable format.

## Setup 🛠️

Clone the repository to your local machine:

```bash
git clone https://github.com/vuthere/Discord-Data-Fetcher.git
cd discord-data-fetcher
```

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Running with Docker 🐳

To encapsulate the environment and simplify the setup, Docker can be used to containerize the application. Here’s how to build and run the Docker container:

1. **Build the Docker Image**:
   ```bash
   docker build -t discord-data-fetcher .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -it discord-data-fetcher
   ```

   For persistent data or sharing files between the host and the container:
   ```bash
   docker run -v $(pwd)/data:/app/data -it discord-data-fetcher
   ```

## Usage 📋

To run the script, use the following command:

```bash
python main.py
```

Upon running, you'll be prompted to enter your Discord token. After authentication, you can:
- Fetch and save your Discord user data 📊.
- Open a specific URL in your default web browser 🌐.

## Windows Executable 🪟

For Windows users, a pre-built executable is available in the releases section of this repository. This executable allows you to run the application without needing to install Python or any dependencies. The executable was compiled with Python 3.10.6.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.