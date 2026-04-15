from flask import Flask, request, jsonify, render_template
import ai_bot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sor", methods=["POST"])
def sor():
    mesaj = request.json.get("mesaj", "")
    cevap = ai_bot.cevap_ver(mesaj)
    return jsonify({"cevap": cevap})

if __name__ == "__main__":
    app.run(debug=True)