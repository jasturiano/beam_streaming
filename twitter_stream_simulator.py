from flask import Flask, request, Response, jsonify
import random
import time
import json


"""
A Flask application that simulates streaming random tweets over an HTTP endpoint.

The application generates random tweet-like messages and streams them to clients that make GET requests to the /stream endpoint.

"""

app = Flask(__name__)

tweets = [
    'RT: One morning, when # Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'
    'He lay on his armour-like back,# and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections.',
    'The bedding was hardly able to cover it and seemed ready to slide off any moment.',
    'RT: His many# legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked.',
    '"What\'s happened to me?" he thought. http://www.ultimate.ai',
    'It wasn\'t a dream.',
    'His room, a proper# human room although a little too small, lay peacefully between its four familiar walls.',
    'A collection of textile samples lay spread out #on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame.\n',
    'It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer.',
    '#Gregor then turned to look out the window at the dull weather.'
]

def send_random_tweet():
    while True:
        random_tweet = random.choice(tweets)
        print(random_tweet)
        yield json.dumps({"data": random_tweet}) + "\n"
        time.sleep(random.uniform(0.5, 4))

@app.route('/stream', methods=['GET'])
def stream_tweets():
    if request.method != "GET":
        return "Only GET requests are accepted", 405
    

    return Response(send_random_tweet(), content_type='application/json')


if __name__ == '__main__':
    app.run(debug=True, host= 'localhost', port= 5555, threaded=True)
    
   