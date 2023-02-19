import os
import time

import requests
import argparse
from bs4 import BeautifulSoup
from revChatGPT.V1 import Chatbot, configure

END_FLAG = "All documents sent"
LINK_TO_CONTENT = "link_to_contents.txt"
LINK_TO_CONTENT_DIR = "link_to_content"


def log(msg):
    print(f"I:{msg}")


class AutoChatBot:
    def __init__(self, base_url, chunk_size, retries, sleep_time, conversation_id):
        self.base_url = base_url
        self.chunk_size = chunk_size
        self.retries = retries
        self.sleep_time = sleep_time
        self.conversation_id = conversation_id
        self.init_chatgpt()

    def extract_text(self, content):
        soup = BeautifulSoup(content, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return " ".join(soup.stripped_strings)

    def scrape_page(self, url):
        log(f"scrape_page: {url}")
        page = requests.get(url)
        return self.extract_text(page.content)

    def fetch_link_contents(self):
        log("fetch_link_contents")
        page_contents = {}
        links = []
        # Fetch the main page
        main_page = requests.get(self.base_url)
        page_contents[self.base_url] = self.extract_text(main_page.content)
        soup = BeautifulSoup(main_page.content, "html.parser")
        # Extract all links from the main page
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and self.base_url in href:
                links.append(href)
        # Fetch the contents of each link
        if len(links) == 0:
            log("not link found, and no contents")
            exit(0)
        for link in links:
            page_contents[link] = self.scrape_page(link)
        # Store the mapping of link to contents
        with open(LINK_TO_CONTENT, "w") as f:
            for link, content in page_contents.items():
                f.write(f"{link}: {content}\n")

    def split_file(self, file_path, output_dir, chunk_size=1024 * 4):
        if not os.path.exists(LINK_TO_CONTENT_DIR):
            os.makedirs(LINK_TO_CONTENT_DIR)
        with open(file_path, "rb") as f:
            chunk = f.read(chunk_size)
            chunk_num = 1
            while chunk:
                output_file = os.path.join(output_dir, f"link_to_contents_{chunk_num}.txt")
                with open(output_file, "wb") as output_f:
                    output_f.write(chunk)
                chunk = f.read(chunk_size)
                chunk_num += 1

    def init_chatgpt(self):
        self.chatbot = Chatbot(configure(), self.conversation_id)
        log("init_chatgpt")

    def chatbot_ask(self, query):
        retries = 0
        while retries < self.retries:
            try:
                data = list(self.chatbot.ask(query))[-1]
                message = data.get("message", "")
                if message:
                    message = "ChatGPT: " + message
                    print(message)
                    if query not in END_FLAG:
                        if "understood" not in message:
                            log("You should only response: Received and understood")
                            self.chatbot_ask("You should only response: Received and understood")
                            retries += 1
                            continue
                break
            except Exception as e:
                log("Error in chatbot_ask: ", str(e))
                retries += 1
        log("Sleep 5 seconds")
        time.sleep(self.sleep_time)

    def send_all_files_to_chatgpt(self):
        path = LINK_TO_CONTENT_DIR
        files = os.listdir(path)
        files.sort(key=lambda x: os.path.getctime(os.path.join(path, x)))
        for filename in files:
            with open(os.path.join(path, filename), "r", encoding="utf-8", errors="replace") as f:
                log(f"Sending file: {filename}")
                content = f.read()
                self.chatbot_ask(content)


# if __name__ == "__main__":
#     # fetch_link_contents()
# split_files()
#     bot = AutoChatBot()
#     log(f"I am going to send you some documents, and you just need say: received and understood, and after all the files sent finished, I will let you know, such as: {END_FLAG}, and later I will ask questions")
#     bot.chatbot_ask(f"I am going to send you some text documents, and you just need say: received and understood, and after all the documents sent finished, I will let you know, such as: {END_FLAG}, and later I will ask questions about those documents")
#     bot.send_all_files_to_chatgpt()
#     log(END_FLAG)
#     bot.chatbot_ask(END_FLAG)
#     log("Summary of the documents I just sent to you")
#     bot.chatbot_ask("Summary of the documents I just sent to you")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch the contents from a website and summarize the contents using OpenAI GPT-3")
    parser.add_argument("--base-url", type=str, default="https://pjq.me/?p=1906",
                        help="The website to fetch the links and contents from")
    parser.add_argument("--chunk-size", type=int, default=1024 * 4, help="The size of each smaller file in bytes")
    parser.add_argument("--retries", type=int, default=2,
                        help="The number of retries when sending a file to the OpenAI GPT-3 model")
    parser.add_argument("--sleep-time", type=int, default=5, help="The time to wait between each file in seconds")

    parser.add_argument(
        "--conversation_id",
        dest="conversation_id",
        type=str,
        default="e226ac01-da16-4e36-8bcc-xxxxxxxxxxx",
        help="ChatGPT conversation_id",
    )
    args = parser.parse_args()

    bot = AutoChatBot(base_url=args.base_url, chunk_size=args.chunk_size, retries=args.retries, sleep_time=args.sleep_time, conversation_id=args.conversation_id)
    bot.fetch_link_contents()
    bot.split_file(LINK_TO_CONTENT, LINK_TO_CONTENT_DIR, args.chunk_size)
    log(f"I am going to send you some documents, and you just need say: received and understood, and after all the files sent finished, I will let you know, such as: {END_FLAG}, and later I will ask questions")
    bot.chatbot_ask(
        f"I am going to send you some text documents, and you just need say: received and understood, and after all the documents sent finished, I will let you know, such as: {END_FLAG}, and later I will ask questions about those documents")
    bot.send_all_files_to_chatgpt()
    log(END_FLAG)
    bot.chatbot_ask(END_FLAG)
    log("Summary of the documents I just sent to you")
    bot.chatbot_ask("Summary of the documents I just sent to you")
