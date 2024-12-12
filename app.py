#!/usr/bin/env python3

from openai import OpenAI
import os
# from flask import Flask, render_template, request, flash
# from flask import redirect, url_for, Request
# import pandas as pd
import time

import settings
logger = settings.logger

# app = Flask(__name__)
# app.secret_key = 'session_secret_key'

client = OpenAI(
    api_key = settings.key

)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        )

    return response.choices[0].message["content"]


if __name__ == "__main__":
    # app.run(debug=True)

    prompt = "What do you know about me?"

    answer = get_completion(prompt)
    logger.info(answer)
    print(answer)