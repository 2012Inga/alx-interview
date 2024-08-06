# Star Wars Characters

This project is a Node.js script that fetches and displays the names of Star Wars characters from a specified movie using the Star Wars API. The script takes a movie ID as a command-line argument and prints the names of all characters featured in that movie.

## Requirements

- Node.js (version 10.x or higher)
- `request` module (for making HTTP requests)

## Installation

### 1. Install Node.js

Ensure that you have Node.js installed on your system. If not, you can install it using the following commands:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

2. Install the request Module
You need to install the request module, which is used to make HTTP requests. Install it globally using:

sudo npm install -g request

or locally in your project directory:

npm install request

3. Make the Script Executable

Ensure that the script file is executale by running:

chmod +x 0-starwars_characters.js

Usage 

Run the script with the movie ID as a command-line argument. For example, to fetch characters from the movie with ID 3, use the following command:

./0-starwars_characters.js 3

Example Output

Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna



Here's a sample README.md file for the "Star Wars Characters" project, which includes information on how to set up and run the script:

markdown
Copy code
# Star Wars Characters

This project is a Node.js script that fetches and displays the names of Star Wars characters from a specified movie using the Star Wars API. The script takes a movie ID as a command-line argument and prints the names of all characters featured in that movie.

## Requirements

- Node.js (version 10.x or higher)
- `request` module (for making HTTP requests)

## Installation

### 1. Install Node.js

Ensure that you have Node.js installed on your system. If not, you can install it using the following commands:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
2. Install the request Module
You need to install the request module, which is used to make HTTP requests. Install it globally using:

bash
Copy code
sudo npm install -g request
Or locally in your project directory:

bash
Copy code
npm install request
3. Make the Script Executable
Ensure that the script file is executable by running:

bash
Copy code
chmod +x 0-starwars_characters.js
Usage
Run the script with the movie ID as a command-line argument. For example, to fetch characters from the movie with ID 3, use the following command:

bash
Copy code
./0-starwars_characters.js 3
Example Output
bash
Copy code
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna


Script Explanation
Imports and Constants:

request: Module used to make HTTP requests.
API_URL: Base URL for the Star Wars API.
Fetch Film Data:

Retrieves film data for the given movie ID.
Extracts the URLs of characters from the film data.
Fetch Character Data:

Uses promises to fetch data for each character URL.
Resolves the promises to get the names of the characters.
Print Character Names:

Prints each character name to the console.

Troubleshooting
Module Not Found: If you encounter Cannot find module 'request', make sure that you have installed the request module. You may need to reinstall it using npm install request.

Node.js Version: Ensure that you are using Node.js version 10.x or higher. Check your Node.js version with node -v.


This `README.md` provides a clear overview of the project, installation instructions, usage guidelines, and troubleshooting tips. Adjust any specifics as needed based on your exact setup or requirements.
