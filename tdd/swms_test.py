import unittest

class WareHouse():

    def __init__(self):
        self.stock = [0, 0, 0]

    def items(self):
        """Returns items in the warehouse."""
        return self.stock
    
    def set_stock(self, item_list):
        self.stock = item_list

    def add_stock(self, item_list):
        if len(self.stock) == len(item_list):
            self.stock = [sum(x) for x in zip(self.stock, item_list)]
        else:
            return False


class TestSWMS(unittest.TestCase):

    def test_keep_track_of_initial_stock(self):
        warehouse = WareHouse()
        self.assertEqual([0, 0, 0], warehouse.items())

    def test_keep_track_changed_stock(self):
        warehouse = WareHouse()
        warehouse.stock = [11, 11, 11]
        self.assertEqual([11, 11, 11], warehouse.items())

    def test_set_items_in_stock(self):
        warehouse = WareHouse()
        warehouse.set_stock([2, 3, 4])
        self.assertEqual([2, 3, 4], warehouse.items())

    def test_add_items_to_stock(self):
        warehouse = WareHouse()
        warehouse.set_stock([1, 2, 3])
        warehouse.add_stock([2, 3, 4])
        self.assertEqual([3, 5, 7], warehouse.items())

    def test_add_wrong_number_of_items_to_stock(self):
        warehouse = WareHouse()
        warehouse.set_stock([1, 2, 3])
        self.assertFalse(warehouse.add_stock([2, 3, 4, 5]), "Length of lists does not match!")

if __name__ == '__main__':
    unittest.main()