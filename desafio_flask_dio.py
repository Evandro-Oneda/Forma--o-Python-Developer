from google.colab.output import eval_js
print (eval_js("google.colab.kernel.proxyPort(5000)"))

dados = [
    {
        "Number": "1",
        "Name": "Mahesh",
        "Age": "25",
        "City": "Bangalore",
        "Country": "India"
    },
    {
        "Number": "2",
        "Name": "Alex",
        "Age": "26",
        "City": "London",
        "Country": "England"
    },
    {
        "Number": "3",
        "Name": "David",
        "Age": "27",
        "City": "San Francisco",
        "Country": "USA"
    },
    {
        "Number": "4",
        "Name": "John",
        "Age": "28",
        "City": "Toronto",
        "Country": "Canada"
    },
    {
        "Number": "5",
        "Name": "Chris",
        "Age": "29",
        "City": "Paris",
        "Country": "France"
    }
]




from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/index") 

def index():
    return (dados)


if __name__ == "__main__":
    app.run(debug=True)

