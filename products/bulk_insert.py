from .models import Category, Product, Condition, Specification, SpecificationValue
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

def bulk_specification():
    Specification.objects.bulk_create(
        [
            Specification(created_time=datetime.now(), title='برند', slug='brand'),
            Specification(created_time=datetime.now(), title='رم', slug='ram'),
            Specification(created_time=datetime.now(), title='پردازشگر مرکزی', slug='cpu'),
            Specification(created_time=datetime.now(), title='حافظه داخلی', slug='hard drive'),
            Specification(created_time=datetime.now(), title='صفحه نمایش', slug='display'),
        ]
    )
    print("bulk Specification inserted!!!")

def bulk_specification_value_brand():
    spec = Specification.objects.get(pk=1)
    SpecificationValue.objects.bulk_create(
        [
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='اپل', slug='apple'),
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='سامسونگ', slug='samsung'),
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='سونی', slug='sony'),
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='هوواویی', slug='hauweii'),
        ]
    )
    print("bulk bulk_specification_value_brand inserted!!!")


def bulk_specification_value_ram():
    spec = Specification.objects.get(pk=2)
    SpecificationValue.objects.bulk_create(
        [
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='۲ گیگابایت', slug='2 GB'),
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='۳ گیگابایت', slug='3 GB'),
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='۴ گیگابایت', slug='4 GB'),
            SpecificationValue(created_time=datetime.now(), specification=spec, display_value='۸ گیگابایت', slug='8 GB'),
        ]
    )
    print("bulk bulk_specification_value_ram inserted!!!")

def bulk_spec_val():
    bulk_specification_value_brand()
    bulk_specification_value_ram()

def bulk_test_data():
    bulk_category()
    bulk_product_tablet()
    bulk_condition()
    bulk_specification()
    bulk_spec_val()


















