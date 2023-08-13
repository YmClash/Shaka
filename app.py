<<<<<<< HEAD
import gradio
import random
import time

=======
import gradio as gr
>>>>>>> origin/main

def greet(name):
    return "Hello " + name + "!!"

<<<<<<< HEAD
def respond(message,chat_history):
    bot_message = random.choice(["Hallo","comment cava ","J'ai faim"])
    chat_history.append((message,bot_message))
    time.sleep(2)
    return "", chat_history



with gradio.Blocks() as app:
    chatbot = gradio.Chatbot(label="Chatbox")
    message = gradio.Textbox()
    bouton_envoye = gradio.Button("Envoyé")
    clear = gradio.ClearButton([message, chatbot])


    bouton_envoye.click(fn=greet, inputs=message, outputs=chatbot)
    message.submit(respond,[message,chatbot],[message,chatbot])

    app.launch(debug=True)
=======
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
>>>>>>> origin/main
