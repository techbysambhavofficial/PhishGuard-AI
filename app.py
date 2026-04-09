from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

# Load model safely
try:
    model = pickle.load(open("model.pkl", "rb"))
    print("✅ Model Loaded Successfully")
except Exception as e:
    print("❌ Model Load Error:", e)
    model = None

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            url = request.form['url']
            print("URL:", url)

            features = extract_features(url)
            print("Features:", features)
            print("Feature Length:", len(features))

            if model is None:
                result = "❌ Model not loaded properly"
            else:
                prediction = model.predict([features])[0]
                prob = model.predict_proba([features])[0]
                confidence = max(prob) * 100

                if prediction == 1:
                    result = f"⚠️ Phishing Website (Confidence: {confidence:.2f}%)"
                else:
                    result = f"✅ Safe Website (Confidence: {confidence:.2f}%)"

        except Exception as e:
            result = f"❌ ERROR: {str(e)}"
            print("Runtime Error:", e)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()