from .models import Category, Product, Condition, Specification, SpecificationValue
from location.models import State, City, Country
from store.models import StoreHouse, CoRepository 
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


def bulk_country():
	Country.objects.bulk_create(
		[
			Country(name='ایران', slug='iran'),
			Country(name='آمریکا', slug='united states'),
			Country(name='انگلیس', slug='england'),
			Country(name='آلمان', slug='Germany'),
		]
	)
	print("bulk bulk_country inserted!!!")


def bulk_state():
	country = Country.objects.get(pk=1)
	print("create states for %s" % country.name)
	State.objects.bulk_create(
		[
			State(name='تهران', slug='tehran',country=country),
			State(name='آذربایجان غربی', slug='west azarbayjan', country=country),
			State(name='آذربایجان شرقی', slug='east azarbayjan', country=country),
		]
	)
	print("bulk bulk_state inserted!!!")


def bulk_city():
	state = State.objects.get(pk=1)
	City.objects.bulk_create(
		[
			City(name='تهران', slug='tehran', state=state),
			City(name='کرج', slug='karaj', state=state),
			City(name='شهریار', slug='shahryiar', state=state),
		]
	)
	print("bulk bulk_city inserted!!!")

def bulk_repository():
    city = City.objects.get(pk=1)
    CoRepository.objects.bulk_create(
        [
            CoRepository(city=city, name="repository1", address="addresssssssssssss1", tel=111111111111),
            CoRepository(city=city, name="repository2", address="addresssssssssssss2", tel=22222222222),
            CoRepository(city=city, name="repository3", address="addresssssssssssss3", tel=3333333333),
            CoRepository(city=city, name="repository4", address="addresssssssssssss4", tel=4444444444),
            CoRepository(city=city, name="repository5", address="addresssssssssssss1", tel=55555555555),
        ]
    )
    print("bulk bulk_repository inserted!!!")

def bulk_store_house():
    repository = CoRepository.objects.get(pk=1)
    product = Product.objects.get(pk=1)
    StoreHouse.objects.bulk_create(
        [
            StoreHouse(repostory=repository, product=product,quantity=1)
        ]
    )
    print("bulk bulk_repository inserted!!!")

def bulk_spec_val():
    bulk_specification_value_brand()
    bulk_specification_value_ram()

def bulk_test_data():
    bulk_category()
    bulk_product_tablet()
    bulk_condition()
    bulk_specification()
    bulk_spec_val()
    bulk_country()
    bulk_state()
    bulk_city()
    bulk_repository()
    bulk_store_house()

















