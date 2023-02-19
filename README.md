# AutoSummaryBot

This is a Python script for fetching documents from the Internet and feeding them to the OpenAI ChatGPT model to summarize the contents. The script consists of several parts:

- Fetching all the links and contents from a website using `requests` and `BeautifulSoup`
- Storing the mapping of links to contents in a text file
- Splitting the text file into smaller files for easier processing
- Sending the smaller files to the OpenAI ChatGPT model using the `revChatGPT` library
- Receiving and printing the summary of the documents from the OpenAI ChatGPT model

## Requirements

- python 3.7+
- requests
- bs4
- revChatGPT

## Usage
1. Install the required libraries:
```
pip3 install requests beautifulsoup revChatGPT
Or
pip instead -r requirements.txt
```
Then follow the revChatGPT to setup the ChatGPT config
- https://github.com/acheong08/ChatGPT

2. Run the script:
```
python3 AutoSummaryBot.py --conversation-id='xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx' --base-url='https://www.google.com/search?q=ChatGPT' --chunk-size=8192
```

The script will first print a message indicating that it is going to send some documents to the OpenAI ChatGPT model. Then it will send the smaller files one by one, and wait for 5 seconds between each file. After all the files are sent, the script will print the message "All documents sent". Finally, it will send a query to the OpenAI ChatGPT model to ask for the summary of the documents, and print the response.

```
I:init_chatgpt
test enable:True
I:I am going to send you some , and you just need say: received and understood, and after all the files sent finished, I will let you know, such as: All documents sent, and later I will ask questions
ChatGPT: Understood. I will only respond with "received and understood" after each text is sent, and await further instructions once you've sent all the documents.
I:Sleep 1 seconds
I:Sending file: link_to_contents_1.txt
ChatGPT: Received and understood.
I:Sleep 1 seconds
I:All documents sent
ChatGPT: Received and understood.
I:Sleep 1 seconds
I:Please help to summarize the content
ChatGPT: The content is about ChatGPT, a chatbot developed by OpenAI and launched in November 2022. It is built on top of OpenAI's GPT-3 family of large language models and has been fine-tuned using both supervised and reinforcement learning techniques. The language model can answer questions, and assist you with tasks such as composing emails, essays, and code. Usage is open to the public for free, while there is also a paid subscription version called ChatGPT Plus. The chatbot is a big deal in the tech industry, and has received attention from various news sources.
I:Sleep 1 seconds
```
## Customization
You can customize the script by changing the following parameters:

- `base_url`: the website to fetch the links and contents from
- `chunk_size`: the size of each smaller file in bytes
- `retries`: the number of retries when sending a file to the OpenAI ChatGPT model
- `sleep_time`: the time to wait between each file in seconds

## Conclusion

This script provides a simple and automated way to fetch documents from the Internet and summarize their contents using the OpenAI ChatGPT model. You can use it as a starting point for your own projects and experiments.



