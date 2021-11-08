from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = (
        {'id':1, 'name': 'Phone', 'barcode':'5959595959', 'price':49999},
        {'id':2, 'name': 'Laptop', 'barcode':'5959595951', 'price':61000},
        {'id':3, 'name':'Headphone', 'barcode':'5959595952', 'price':11000},
    )
    return render_template('market.html', items=items)

@app.route('/diwali')
def diwali():
    return "Shubh Deppawali, God Bless us."



if __name__ == "__main__":
    app.run(debug=True)