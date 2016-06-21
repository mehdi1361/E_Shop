from .models import Category, Product, Condition
from datetime import datetime

def bulk_category():
    Category.objects.bulk_create(
            [
                Category(name='لوازم الکترونیک'),
                Category(name='ارتباطات'),
                Category(name='موبایل و تبلت'),
                Category(name='موبایل'),
                Category(name='تبلت'),
            ]
    )
    print("bulk category inserted!!!")



def bulk_product_tablet():
    category = Category.objects.get(pk=5)
    Product.objects.bulk_create(
            [
                Product(name='Galaxy tab s2',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy tab s1',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy tab s3',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy note1',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy note1',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy note1',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy note2',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy note3',created_at=datetime.now(),is_container = True,category=category),
                Product(name='Galaxy note4',created_at=datetime.now(),is_container = True,category=category),
                Product(name='xpreia z',created_at=datetime.now(),is_container = True,category=category),
                Product(name='xperia zl',created_at=datetime.now(),is_container = True,category=category),
            ]
    )
    print("bulk Product inserted!!!")


def bulk_condition():
    Condition.objects.bulk_create([
            Condition(title="نو", slug="new"),
            Condition(title="در حد نو", slug="semi new"),
            Condition(title="دست دوم", slug="stock"),
        ])
    print("bulk Condition inserted!!!")


def bulk_test_data():
    bulk_category()
    bulk_product_tablet()
    bulk_condition()












