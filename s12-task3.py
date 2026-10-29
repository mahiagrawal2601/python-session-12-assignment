products = ['Samsung Mobile', 'shoes', 'iPhone', 'smart watch', 'headphones']

flipkart_product = list(filter(lambda product : product.lower().startswith("s"), products))

print(flipkart_product)