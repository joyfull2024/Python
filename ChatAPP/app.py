from g4f.client import Client
import gradio as gr

client = Client()

def generate_writing_prompt(user_input):
   response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}],
    )
   return response.choices[0].message.content


interface = gr.Interface(
   fn=generate_writing_prompt,
   inputs=gr.Textbox(lines=3, placeholder="Type your question here..."),
   outputs="text",
   title="Creative Assistant Assistance",
   description="Ask any question and the AI assistant will response?",
   theme="huggingface",
   examples=[
      ["A story about a lost civilization discovering technology."],      
      ["Compost a poem the changing seasons."],
      ["Write a Prompt for a blog SEO friendly content."]

   ]
)
   
#launch the Interface
if __name__ == "__main__":
   interface.launch()