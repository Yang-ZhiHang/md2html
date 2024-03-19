from flask import Flask, request, render_template, jsonify, Blueprint
from md2html import parse_markdown_to_html
from flask_cors import CORS
from flask_docs import ApiDoc

app = Flask(__name__)
app.config["API_DOC_MEMBER"] = ["API"]
CORS(app)
ApiDoc(
    app,
    title="API Documents",
    version="1.0.0",
    description="A simple app API of markdown to html",
)
api = Blueprint("API", __name__)


@app.get('/')
def default_page():
    return render_template("index.html")


@app.get('/parse')
def md2html():
    filename = request.args.get('filename')
    html = parse_markdown_to_html(filename)
    return html


@api.route("/md2html", methods=["GET"])
def Md2html():
    """
    turn md to html

    @@@
    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    | filename |   false  |      None    | str  |  None   |

    ### request
    ```json
    {"filename": "[markdown_name]"}
    ```

    ### return
    ```json
    {"data": [html code]}
    ```
    @@@
    """
    return jsonify({"API": "MD2HTML"})


app.register_blueprint(api, url_prefix="/API")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
