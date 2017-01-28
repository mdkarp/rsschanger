from flask import Flask, request, render_template, redirect, url_for, make_response
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

    r = make_response(render_template('rss.xml', feed=thisfeed['feed'], entries=thisfeed['entries']))
    r.headers.set('Content-type', "text/xml")
    return r


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
