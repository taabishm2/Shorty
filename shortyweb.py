from flask import Flask, render_template, url_for, request
import shorty

app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def main():
    inp = request.form

    if len(inp) == 0:
        return render_template('index.html')

    link = inp['inputlink']
    if shorty.validate_url.validate_url(link):
        vlink = link
        rcode = shorty.url_encode(link)
    else:
        rcode = shorty.url_decode(link)
        vlink = rcode

    return render_template('index.html',slink=rcode,vlink=vlink)

@app.route("/converted", methods=['POST','GET'])
def convert():
    inp = request.form
    link = inp['inputlink']

    if shorty.validate_url.validate_url(link):
        rcode = shorty.url_encode(link)
    else:
        rcode = shorty.url_decode(link)

    return render_template('converted.html',link=rcode)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
