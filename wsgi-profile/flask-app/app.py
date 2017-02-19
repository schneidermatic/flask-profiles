from flask import Flask, request, redirect

import urlparse

app = Flask(__name__) 

@app.route('/')
@app.route('/<path:path>')
def https_redirect(path='/'):
    url = urlparse.urlunparse((
        'https',
        request.headers.get('Host'),
        path,
        '','',''
    ))

    return redirect('https://0.0.0.0:8443', code=301)


if __name__ == '__main__':
    app.run()
