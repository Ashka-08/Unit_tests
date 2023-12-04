class Shop:

    def __init__(self, products: list):
        self.__products = products

    def get_products(self):
        return self.__products

    def set_products(self, products):
        self.__products = products

    # @return отсортированный по возрастанию и цене список продуктов
    def get_sorted_list_products(self):
        return sorted(self.__products, key=lambda x: x.get_cost())

    # @return самый дорогой продукт
    def get_most_expensive_product(self):
        return max(self.__products, key=lambda x: x.get_cost())