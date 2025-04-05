from config.dependencies import db
from models.models import Category, Item

def get_all_categories():
    categories = db.query(Category).all()
    return categories

def get_all_line_items():
    line_items = db.query(Item).all()
    return line_items
