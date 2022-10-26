from flask import  render_template
from DemoSaleApp import app, utils

@app.route("/")
def home():
    # categories = utils.load_categories() categories = categories,
    products = utils.load_products()
    return render_template('index.html',
                           products = products
                           )
if __name__ == '__main__':
    app.run(debug=True)