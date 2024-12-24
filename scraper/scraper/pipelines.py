import sqlite3

class DealsPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('../../database/deals.db')
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute('''
                INSERT INTO deals (product_name, price, retailer, link)
                VALUES (?, ?, ?, ?)
            ''', (item['product_name'], item['price'], item['retailer'], item['link']))
            self.connection.commit()
            print(f"Inserted item: {item['product_name']}")
        except sqlite3.IntegrityError as e:
            print(f"Failed to insert item: {item}, error: {e}")
        return item
