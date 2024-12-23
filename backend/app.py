from flask import Flask, request, jsonify
import sqlite3
from scheduler import start_scheduler

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('../database/deals.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get all deals
@app.route('/deals', methods=['GET'])
def get_deals():
    conn = get_db_connection()
    deals = conn.execute('SELECT * FROM deals').fetchall()
    conn.close()
    return jsonify([dict(deal) for deal in deals])

# Add a new deal
@app.route('/deals', methods=['POST'])
def add_deal():
    new_deal = request.get_json()
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO deals (product_name, price, retailer, link)
        VALUES (?, ?, ?, ?)
    ''', (new_deal['product_name'], new_deal['price'], new_deal['retailer'], new_deal['link']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deal added successfully!'}), 201

# Update a deal
@app.route('/deals/<int:id>', methods=['PUT'])
def update_deal(id):
    updated_deal = request.get_json()
    conn = get_db_connection()
    conn.execute('''
        UPDATE deals SET product_name = ?, price = ?, retailer = ?, link = ?
        WHERE id = ?
    ''', (updated_deal['product_name'], updated_deal['price'], updated_deal['retailer'], updated_deal['link'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deal updated successfully!'})

# Delete a deal
@app.route('/deals/<int:id>', methods=['DELETE'])
def delete_deal(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM deals WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deal deleted successfully!'})

if __name__ == '__main__':
    start_scheduler()
    app.run(debug=True)
