# from collections import namedtuple

# Product = namedtuple('Product', ['name', 'description', 'price', 'quantity'])

# smartphone = Product(name = 'iphone 16', description = 'iphone 16', price = 1000, quantity = 5)

# product_data_as_dict = Product._asdict(smartphone)
# print(product_data_as_dict)

# smarthphone = smartphone._replace(name = 'samsung', price = 600)
# print(smarthphone)

# print(f'Product fields: {Product._fields}')


# git config --global user.name 'Javohir'
# git config --global user.email 'javohir@gmail.com'



import pyttsx3
engine = pyttsx3.init()
engine.say("hahaha")
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()