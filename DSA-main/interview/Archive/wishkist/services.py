class User:

    def __init__(self, name, id):
        self.name=name 
        self.id=id

class Item:
    Item_name: str
    item_id: int 
    price: int

class Wishlist:
    wishlist_id: int
    user_id: User 
    item_id: Item
    item_soft_deleted: bool=False 
    total_cost: int


class WishlistCreation():

    def calculate_total_wishlist(wishlist_id):
        total_value = 0
        for i in range(len(wishlist_id)):
            total_value = total_value + i.item_id.price
        return total_value


    def add_item_to_wishlist(user_id, item_id, wishlist_id):
        if user_id not in User:
            raise "No user found"
        if item_id not in Item:
            raise "No item found"
        if wishlist_id not in Wishlist:
            raise "No wishlist found"
        if item_id in Wishlist.item_id:
            raise "Item already exists"
        Wishlist.insert(user_id, item_id, wishlist_id)
        Wishlist.total_cost = calcualate_total_wishlist(wishlist_id)

    
    def delete_item(user_id, item_id, )
