from flask import Blueprint, jsonify
from app.cache import cache
from app.services import get_financial_data

bp = Blueprint('routes', __name__)

@bp.route('/prices', methods=['GET'])
@cache.cached(timeout=600)
def get_prices():

    try:
        data = get_financial_data()
        return jsonify({
            "brent_price": data["brent_price"],
            "dollar_price": data["dollar_price"]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
