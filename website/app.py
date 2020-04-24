
import flask
import pandas as pd
import praw
from praw.models import MoreComments
import textcleaning as tc
import pickle


model = pickle.load(open('models/RF.pkl', 'rb'))

reddit = praw.Reddit(client_id='OLWVW-YovatlVA',
                     client_secret='cTA25hqDeIlzYxSBhmAk6dq1Vyo',
                     user_agent='Reddit-Scrapper')


def prediction(url):
    submission = reddit.submission(url=url)
    data = {}
    data['title'] = str(submission.title)
    data['url'] = str(submission.url)
    data['body'] = str(submission.selftext)

    submission.comments.replace_more(limit=None)
    comment = ''
    count = 0
    for top_comment in submission.comments:
        comment = comment+''+top_comment.body
        count += 1
        if(count > 10):
            break

    data['comment'] = str(comment)
    data['title'] = tc.clean_text(str(data['title']))
    data['body'] = tc.clean_text(str(data['body']))
    data['comment'] = tc.clean_text(str(data['comment']))

    combined_features = data['title']+data['comment']+data['body']+data['url']

    return model.predict([combined_features])


app = flask.Flask(__name__, template_folder='templates')

# setup the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        text = flask.request.form['url']
        flair = prediction(str(text))

        return flask.render_template('result.html', original_input={'url': str(text)}, result=flair,)


if __name__ == '__main__':
    app.run()
