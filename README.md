# Pcap filter with GPT

## Setting up your OPEN_API_KEY
You will need to create a `.env` file at the root of the project. After that, write the following line in it:

```env
OPENAI_API_KEY="YOUR KEY"
```
The `.env` file will not be pushed to Github, therefore your API key will not be shown in the repository.

## Setting up your MySQL username and password
Inside the same `.env` file created before, add the following:
```env
MYSQL_USER="XXX"
MYSQL_PASSWORD="XXX"
```
The `.env` file will not be pushed to Github, therefore your user and password will not be shown in the repository.