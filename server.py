from flask import Flask, request, render_template, redirect, url_for
import feedparser
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route('/rss')
def rsschanger():
    rss_url = request.args.get('rss')
    if not rss_url:
        return redirect(url_for('hello'))

    thisfeed = feedparser.parse(rss_url)
    entries = thisfeed['entries']

    return render_template('rss.xml')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
