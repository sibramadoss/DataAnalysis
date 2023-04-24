import os
import openai

openai.api_key = ('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')

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role" : "user", "content" : "what is the circumference of the moon in km"}]
)

print(completion)



