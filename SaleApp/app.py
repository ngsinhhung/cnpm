from flask import Flask, render_template, request

import dao

app = Flask(__name__)


@app.route('/')
def index():
    q = request.args.get('q')
    cate_id = request.args.get('category_id')

    categories = dao.load_categories()
    products = dao.load_products(q, category_id=cate_id)
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def details(product_id):
    detail_product = dao.load_product_detail(product_id)
    return render_template('details.html', detail=detail_product)

@app.context_processor
def config_processor():
    return {
        "categories": dao.load_categories()
    }

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
