from flask import Flask, render_template
import random, socket

hostname = socket.gethostname()

app = Flask(__name__)

# list of cat images
images = [
    "https://i0.wp.com/media0.giphy.com/media/C9o0hV1zdqHwQ/giphy.gif",
    "https://media.tenor.com/images/01c9335a75f986e718f4a2330f111c87/tenor.gif",
    "https://78.media.tumblr.com/711f94e0d55af49b9c2cbb6596563a1a/tumblr_nhkimytPhI1u302mqo1_400.gif",
    "https://78.media.tumblr.com/f7290c179becf2439252981729c088d3/tumblr_nyawibb4kU1qbxi45o3_500.gif",
    "https://78.media.tumblr.com/798937b68b2a49f45760e75bef29175a/tumblr_oibyt2Axz61u30qlso1_250.gif",
    "https://78.media.tumblr.com/b8b2b19fe036aefcb438de7ba2f7a53a/tumblr_nzgcqq8IPp1qarjjvo1_400.gif",
    "https://78.media.tumblr.com/bc0c6c4a5df248e69b1379da56a75cf4/tumblr_nyjslqJdS31qbxi45o1_500.gif",
    "https://78.media.tumblr.com/f72fe94c23b6fcf623a08c6126762956/tumblr_nz75xzWFmo1tpri36o1_250.gif",
    "https://78.media.tumblr.com/d651183169f1f67b55d4a830923c6fce/tumblr_nzwghk0LUx1u7gnm9o1_500.gif",
    "https://78.media.tumblr.com/cf441d245c59d6a0cf86d4ad391c0743/tumblr_oifs06ajcn1tpri36o1_400.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")