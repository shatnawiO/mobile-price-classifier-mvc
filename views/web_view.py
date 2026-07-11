from flask import Flask, request, render_template
from controllers.predict_controller import get_prediction
from models.preprocessing import FEATURE_COLUMNS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        raw_data = {col: [float(request.form[col])] for col in FEATURE_COLUMNS}
        result = get_prediction(raw_data)
    return render_template("index.html", columns=FEATURE_COLUMNS, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
