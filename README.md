Phishing Website Detection System 🛡️

A Machine Learning based web application that detects whether a given website URL is phishing (malicious) or legitimate (safe).

This project uses Python, Flask, and Random Forest to analyze URL based features and predict whether a website is safe or suspicious.

PROJECT OVERVIEW

Phishing websites are fake websites designed to steal sensitive information such as passwords, OTPs, banking details, and personal data.

This system helps users by analyzing a website URL and predicting whether it is:

Legitimate Website (Safe)
Phishing Website (Malicious)

The prediction is made using a trained Machine Learning model.

PROJECT STRUCTURE

PHISHING_DETECTOR/

├── app.py
├── train_model.py
├── feature_extraction.py
├── model.pkl
├── templates/
│ └── index.html
├── screenshots/
├── dataset_sample.csv
├── .gitignore
├── README.md
├── allfiles.txt
└── bigobjects.txt

FEATURES

Detects phishing and legitimate URLs
Uses Random Forest Classifier
Flask based web interface
URL feature extraction system
Fast and simple prediction
Beginner friendly project structure

MACHINE LEARNING MODEL

Algorithm Used: Random Forest Classifier

Input: Website URL

Output:

0 = Legitimate Website
1 = Phishing Website

TECHNOLOGIES USED

Python
Flask
Scikit-learn
Pandas
NumPy
HTML
CSS

WHY dataset.csv IS REMOVED FROM GITHUB

The original dataset.csv file is large in size, so it has been removed from this repository to keep the project lightweight and GitHub friendly.

Large files can:

Slow down repository loading
Increase upload time
Cause GitHub size issues

You can use your own dataset or create a new dataset with the same format.

SAMPLE DATASET FORMAT

Create a file named:

dataset_sample.csv

Use this format:

URL,Label
https://google.com,good

https://github.com,good

https://amazon.in,good

http://paypal-login-secure-update.xyz,bad

http://freegift-win-now.tk,bad

http://bank-verification-alert.cf,bad

Label Meaning:

good = Legitimate Website
bad = Phishing Website

If needed, rename dataset_sample.csv to dataset.csv before training.

HOW TO RUN THE PROJECT

Install Dependencies

pip install flask pandas numpy scikit-learn

Train the Model (Optional)

python train_model.py

This will generate:

model.pkl

Run the Flask App

python app.py

Open in Browser

http://127.0.0.1:5000/

SCREENSHOTS

Project screenshots are available inside the screenshots folder.

ACADEMIC USE

This project is suitable for:

B.Tech Mini Project
Machine Learning Project
Cyber Security Project
Final Year Project
Semester Submission

AUTHOR

Sambhav Raj

B.Tech Student
Cyber Security | Machine Learning | Web Development

LICENSE

This project is for educational purposes only.
