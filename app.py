from urllib import response
from g4f.client import Client
import gradio as gr
from matplotlib import lines

client = Client()

def chatbot_response(user_input):
   response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}],
)
   return response.choices[0].message.content


interface = gr.Interface(
   fn=chatbot_response,
   inputs=gr.Textbox(lines=2, placeholder="Type your question here..."),
   outputs="text",
   title="AI Assistant Chatbot",
   description="Ask any question and the AI assistant will response."
)

#launch the Interface
if __name__ == "__main__":
   interface.launch()