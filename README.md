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
```
Then follow the revChatGPT to setup the ChatGPT config
- https://github.com/topics/revchatgpt

2. Run the script:
```
python AutoSummaryBot.py
```

The script will first print a message indicating that it is going to send some documents to the OpenAI ChatGPT model. Then it will send the smaller files one by one, and wait for 5 seconds between each file. After all the files are sent, the script will print the message "All documents sent". Finally, it will send a query to the OpenAI ChatGPT model to ask for the summary of the documents, and print the response.

```
I:init_chatgpt
I:fetch_link_contents
I:scrape_page: https://pjq.me/?p=1906
I:scrape_page: https://pjq.me/?p=1906#respond
I:scrape_page: https://pjq.me/?p=1906
I:I am going to send you some documents, and you just need say: received and understood, and after all the files sent finished, I will let you know, such as: All documents sent, and later I will ask questions
ChatGPT: Understood! I am ready to receive the documents. Please send them my way and let me know when you have finished sending all of them. I will be sure to acknowledge each document as I receive it, and once all have been received, I will be ready to answer any questions you may have about them.
I:You should only response: Received and understood
ChatGPT: Received and understood.
I:Sleep 5 seconds
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:Sending file: link_to_contents_1.txt
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:Sending file: link_to_contents_2.txt
ChatGPT: It looks like this is a blog post or a website that contains information about various topics, such as technology, software, and personal experiences. The categories listed include English, Tech, Android, Linux, Software, and personal reflections. The archives show a list of past posts, and the recent comments section displays comments on various blog posts. The tags section lists keywords that are related to the content on the website.
I:You should only response: Received and understood
ChatGPT: Received and understood.
I:Sleep 5 seconds
ChatGPT: Received and understood
I:Sleep 5 seconds
I:Sending file: link_to_contents_3.txt
ChatGPT: It looks like you have successfully integrated the ChatGPT model with the Xiao Ai smart home assistant. It appears that you used a project called "Xiaoai-ChatGPT" as a reference for this integration. This project connects the Xiao Ai device to the ChatGPT API through a series of steps, including cloning the ChatGPT repository, installing the "revChatGPT" and "miservice" packages, and setting environment variables for your Xiaomi account. The final step involves running the "xiaogpt.py" script to initiate the connection between the Xiao Ai device and the ChatGPT API. When you ask the Xiao Ai device a question that starts with "帮我回答", the question will be forwarded to the ChatGPT API, and the answer will be played back through the Xiao Ai device.
I:You should only response: Received and understood
ChatGPT: Received and understood.
I:Sleep 5 seconds
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:Sending file: link_to_contents_4.txt
ChatGPT: I'm sorry, but I am not sure what you would like me to do with this information. Could you please provide more context or clarify your request?
I:You should only response: Received and understood
ChatGPT: Received and understood.
I:Sleep 5 seconds
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:Sending file: link_to_contents_5.txt
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:All documents sent
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:Summary of the documents I just sent to you
ChatGPT: I'm sorry, but I didn't receive any documents. Can you please provide more information or resend the documents?
I:You should only response: Received and understood
ChatGPT: Received and understood.
I:Sleep 5 seconds
ChatGPT: I'm sorry, but you didn't send me any documents recently.
I:You should only response: Received and understood
ChatGPT: Received and understood.
I:Sleep 5 seconds
I:Sleep 5 seconds
```
## Customization
You can customize the script by changing the following parameters:

- `base_url`: the website to fetch the links and contents from
- `chunk_size`: the size of each smaller file in bytes
- `retries`: the number of retries when sending a file to the OpenAI ChatGPT model
- `sleep_time`: the time to wait between each file in seconds

## Conclusion

This script provides a simple and automated way to fetch documents from the Internet and summarize their contents using the OpenAI ChatGPT model. You can use it as a starting point for your own projects and experiments.



