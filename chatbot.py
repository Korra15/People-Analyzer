from flask import Blueprint, render_template, request
from flask_login import login_required



from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings


warnings.filterwarnings('ignore')


chatbot = Blueprint('chatbot', __name__)


@chatbot.route("/chat", methods=['POST', 'GET'])
@login_required
def chat():
    # Download the punkt package
    nltk.download('punkt', quiet=True)

    # get the article
    article = Article('https://www.simplypsychology.org/big-five-personality.html')
    article.download()
    article.parse()
    article.nlp()
    corpus = article.text
    # print fetched data
    # print(corpus)
    # tokenization
    text = corpus
    sens_lst = nltk.sent_tokenize(text)  # sentense list

    a1 = Article('https://www.verywellmind.com/the-big-five-personality-dimensions-2795422')
    a1.download()
    a1.parse()
    a1.nlp()
    corpus = a1.text
    text = corpus
    sens_lst.append(text)

    a2 = Article('https://www.123test.com/personality-agreeableness/')
    a2.download()
    a2.parse()
    a2.nlp()
    corpus = a2.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3833658/#:~:text=available%20upon%20request.-,Antagonism,traits%20(see%20Figure%204).')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)
    
    a5 = Article('https://www.britannica.com/topic/personality')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://en.wikipedia.org/wiki/Personality')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://www.merriam-webster.com/dictionary/personality')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://en.wikipedia.org/wiki/Openness_to_experience')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://en.wikipedia.org/wiki/Conscientiousness')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://en.wikipedia.org/wiki/Extraversion_and_introversion')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)


    a5 = Article('https://en.wikipedia.org/wiki/Agreeableness')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    a5 = Article('https://en.wikipedia.org/wiki/Neuroticism')
    a5.download()
    a5.parse()
    a5.nlp()
    corpus = a5.text
    text = corpus
    sens_lst.append(text)

    # returns a random greeting response
    def greeting_resp(text):
        text = text.lower()
        b_greetings = ['howdy', 'hi', 'hello', 'hey', 'namaste', 'ciao']
        u_greeting = ['hi', 'hello', 'hey',
                      'greetings', 'wassup', 'ciao', 'namaste']
        for wrd in text.split():
            if wrd in u_greeting:
                return random.choice(b_greetings)

    def idx_sort(list_var):
        leng = len(list_var)
        list_idx = list(range(0, leng))
        x = list_var
        for i in range(leng):
            for j in range(leng):
                if x[list_idx[i]] > x[list_idx[j]]:
                    # swap
                    temp = list_idx[i]
                    list_idx[i] = list_idx[j]
                    list_idx[j] = temp
        return list_idx

    # Create bot response
    def b_response(u_ip):
        u_ip = u_ip.lower()
        sens_lst.append(u_ip)
        b_response = ''
        cm = CountVectorizer().fit_transform(sens_lst)
        similarity_scores = cosine_similarity(cm[-1], cm)
        similarity_scores_list = similarity_scores.flatten()
        idx = idx_sort(similarity_scores_list)
        idx = idx[1:]
        resp_flag = 0

        j = 0  # give top two similar sentences
        for i in range(len(idx)):
            if similarity_scores_list[idx[i]] > 0.0:
                b_response = b_response+' '+sens_lst[idx[i]]
                resp_flag = 1
                j = j + 1
            if j > 2:
                break
            if resp_flag == 0:
                b_response = b_response+' '+"I apoligize, I don't understand"
                break

            # sens_lst.remove(u_ip)
        return b_response

    ex_ls = ['exit', 'see you later', 'bye',
             'quit', 'break', 'terminate', 'adios']

    if request.method == 'GET':
        return render_template("chatBot.html")

    if request.method == 'POST':
        text1 = request.form.get('textbox')
        while(True):
            u_ip = text1
            if u_ip.lower() in ex_ls:
                ans = str('See you later!')
                break
            else:
                if greeting_resp(u_ip) != None:
                    ans = str(greeting_resp(u_ip))
                    break
                else:
                    ans = str(b_response(u_ip))
                    break
        return render_template("chatBot.html", output=ans, user_text=text1)
