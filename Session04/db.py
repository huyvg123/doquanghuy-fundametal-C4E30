import pymongo

client = pymongo.MongoClient("mongodb+srv://doquanghuy:vYaFKXSauCOe4CjC@cluster0-hnp3z.mongodb.net/test?retryWrites=true")
db = client.test

def update(name,price): 
    db.foods.update_one({'name':name,{'$set':{'price':price}}})

def get_food_by_name(name):
    return db.foods.find_one({'name':name}) 


def get_all(): 
    """
    Lấy tất cả các food
    """
    return list(db.foods.find({}))

def add_food(name,price): 
    db.foods.insert_one({'name':name, 'price':price})
# db.foods.save({'name':'cơm rang','price':20})
# #thêm vào 1 
# db.foods.insert_one({'name' : 'Hoa', 'age' : 30})


# #tìm kiếm users có tên Hoa
# print(list(db.foods.find({'name':'Hoa'})))
# #tìm kiếm 1 user có tên Hoa
# print(db.foods.find_one('name':'Hoa'))

# #update users có tên "Hoa" thành 40
# print(db.foods.update_one({"name":"Hoa"},{"$set":{"age":40}}))

# #xóa đi phần tử có tên là Hoa
# db.foods.delete_one({'name':'Hoa'})