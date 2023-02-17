# AutoSummaryBot

This is a Python script for fetching documents from the Internet and feeding them to the OpenAI GPT-3 model to summarize the contents. The script consists of several parts:

- Fetching all the links and contents from a website using `requests` and `BeautifulSoup`
- Storing the mapping of links to contents in a text file
- Splitting the text file into smaller files for easier processing
- Sending the smaller files to the OpenAI GPT-3 model using the `revChatGPT` library
- Receiving and printing the summary of the documents from the OpenAI GPT-3 model

## Requirements

- python 3.7+
- requests
- bs4
- revChatGPT

## Usage
1. Install the required libraries:
```
pip3 install requests beautifulsoup revChatGPT
```
Then follow the revChatGPT to setup the ChatGPT config
- https://github.com/topics/revchatgpt

2. Run the script:
```
python AutoSummaryBot.py
```

The script will first print a message indicating that it is going to send some documents to the OpenAI GPT-3 model. Then it will send the smaller files one by one, and wait for 5 seconds between each file. After all the files are sent, the script will print the message "All documents sent". Finally, it will send a query to the OpenAI GPT-3 model to ask for the summary of the documents, and print the response.

## Customization(Not Supported Yet)
You can customize the script by changing the following parameters:

- `base_url`: the website to fetch the links and contents from
- `chunk_size`: the size of each smaller file in bytes
- `retries`: the number of retries when sending a file to the OpenAI GPT-3 model
- `sleep_time`: the time to wait between each file in seconds

## Conclusion

This script provides a simple and automated way to fetch documents from the Internet and summarize their contents using the OpenAI GPT-3 model. You can use it as a starting point for your own projects and experiments.



