import os
import time

import requests
from bs4 import BeautifulSoup
from revChatGPT.V1 import Chatbot, configure

END_FLAG="All documents sent"

def log(msg):
    print(f"I:{msg}")

class AutoChatBot:
    def __init__(self):
        self.init_chatgpt()

    def extract_text(self, content):
        soup = BeautifulSoup(content, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return " ".join(soup.stripped_strings)

    def scrape_page(self,url):
        page = requests.get(url)
        return self.extract_text(page.content)

    def fetch_link_contents(self):
        base_url = "https://pjq.me/"
        page_contents = {}
        links = []
        # Fetch the main page
        main_page = requests.get(base_url)
        soup = BeautifulSoup(main_page.content, "html.parser")
        # Extract all links from the main page
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and base_url in href:
                links.append(href)
        # Fetch the contents of each link
        for link in links:
            page_contents[link] = self.scrape_page(link)
        # Store the mapping of link to contents
        with open("link_to_contents.txt", "w") as f:
            for link, content in page_contents.items():
                f.write(f"{link}: {content}\n")

    def split_file(file_path, output_dir, chunk_size=1024 * 4):
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
        self.chatbot = Chatbot(configure())
        log("init_chatgpt")

    def chatbot_ask(self, query):
        retries = 0
        while retries < 2:
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
        time.sleep(5)

    def send_all_files_to_chatgpt(self):
        path = "link_to_contents"
        files = os.listdir(path)
        files.sort(key=lambda x: os.path.getctime(os.path.join(path, x)))
        for filename in files:
            with open(os.path.join(path, filename), "r", encoding="utf-8", errors="replace") as f:
                log(f"Sending file: {filename}")
                content = f.read()
                self.chatbot_ask(content)

if __name__ == "__main__":
    # fetch_link_contents()
    # split_files()
    bot = AutoChatBot()
    log(f"I am going to send you some documents, and you just need say: received and understood, and after all the files sent finished, I will let you know, such as: {END_FLAG}, and later I will ask questions")
    bot.chatbot_ask(f"I am going to send you some text documents, and you just need say: received and understood, and after all the documents sent finished, I will let you know, such as: {END_FLAG}, and later I will ask questions about those documents")
    bot.send_all_files_to_chatgpt()
    log(END_FLAG)
    bot.chatbot_ask(END_FLAG)
    log("Summary of the documents I just sent to you")
    bot.chatbot_ask("Summary of the documents I just sent to you")


# if __name__ == "__main__":
#     # main()
#     splitfile2()
