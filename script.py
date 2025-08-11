import json
import random
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

books = {"bbd": json.load(open("books/bbd.json", "r")), "ttpm": json.load(open("books/ttpm.json", "r")), "ktrop": json.load(open("books/ktrop.json", "r"))}

random_book = random.choice(list(books.keys()))
random_chapter = books[random_book]["chapters"][random.choice(range(len(books[random_book]["chapters"])))]

client = Groq(api_key=os.environ["GROQ_API"])
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
    {
      "role": "system",
      "content": (
          "You are a helpful assistant. You will be given a chapter from a random book "
          "and you will generate one important part of the whole from it. The size of "
          "that text must be in single paragraph retrived directly from the chapter, "
          "until the context is properly delivered. The format of the text must be in a "
          "single paragraph. That part should be relevant to the chapter's themes and "
          "messages. The output should be in JSON format with the key 'quotations' containing "
          "a list of strings, chapter name, and book title. Please only retrieve text from "
          "the chapter and do not include any additional information or context and also "
          "without json code block. Consider the json format to be like this: {\"quotations\": "
          "[\"<quote>\"], \"chapter_name\": \"<chapter_name>\", \"book_title\": \"<book_title>\"}. "
          "The quote should be a single paragraph from the chapter that is relevant to the "
          "chapter's themes and messages."
      )
    }, 
        {
            "role": "user",
            "content": f'{{"book_title": "{books[random_book]["title"]}", "chapter_name": "{random_chapter["title"]}", "chapter_text": "{random_chapter["content"]}"}}'
        }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stop=None,
    response_format={"type": "json_object"}
)

mail_content = (json.loads(completion.choices[0].message.content))

print((mail_content))