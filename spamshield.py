import gradio as gr

spam_words = {
    'free': 1, 'claim': 2, 'winner': 3, 'prize': 2, 'click': 1, 'buy': 1, 'cheap': 1, 'limited': 2, 'offer': 2, 'urgent': 3
}


threshold = 4
def check(mess):
    words = mess.lower().split()
    flagged = []
    for word in words:
        word = word.strip(":,.!?/:;'\"")
        if(word in spam_words):
            flagged.append(word)

    score = sum(spam_words[word] for word in flagged)
    result = 'Spam' if score >= threshold else 'Safe'
    return result, score, ' , '.join(flagged)

app = gr.Interface(fn=check, inputs=gr.Textbox(lines=2, label='Enter your message'), outputs=[gr.Textbox(lines=3, label = 'Verdict'), gr.Number(label="Spam score"), gr.Textbox(label='flagged words')], title='Spam Shield', description= "Let's detect spams", examples=[['Congratulations! You won a cash prize!'],['Hi, are we meething today?'],['Limited time offer! Buy now!']])

app.launch()
