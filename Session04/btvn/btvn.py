#ex1: 
import pymongo

client = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db = client.c4e

#ex2: 
the_blog = {
    'title' : 'Tâm sự của học viên',
    'author' : 'Đỗ Quang Huy',
    'content' : 'thằng nào bảo code dễ em táng vỡ mặt nó cho anh =))) . Học ở Mindx vui lắm, có anh hướng dẫn, chị quản lí vui tính và anh trợ giảng khá nhiệt tình nên không phải lo nhé ;)'
}
db.posts.insert_one(the_blog)