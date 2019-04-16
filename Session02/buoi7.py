from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
<title>Trang web của tôi</title>
<body>
    <h1>Chào mừng đến với Techkids</h1>
    <p id='data'>Xin chào</p>
    <p>python</p>
    <p>c#</p>
    <p>java</p>
    
    <div>
        <div  data="tin_tuc">
            <a href='http://google.com'>Tự động hóa xét nghiệm, giảm chờ đợi cho người bệnh</a>
            <div>   
                <p>Bệnh viện Chợ Rẫy vừa đưa hệ thống xét nghiệm tự động hóa hoàn toàn thứ 2 </p>
            </div>
        </div>
        <div  data="tin_tuc">
            <a href='http://google.com'>Bất ngờ với những lợi ích sức khỏe khi ăn ớt</a>
            <div>   
                <p>Có rất nhiều lý do tốt để thêm ớt vào chế độ ăn và con số này tiếp tục tăng lên </p>
            </div>
        </div>
    </div>
 
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
x = soup.find_all('div',{'id'='content'})

x = list(x)
rint(list())

soup = BeautifulSoup(html, 'html.parser') # Sau dòng này thì soup chính là cả document.
print("------------Lấy title:", soup.title)  # do title là con đầu tiên của document
print("------------Lấy riêng text của title", soup.title.string) # .string sẽ lấy ra nội dung text của thẻ

# .p sẽ ra thẻ đầu tiên nó tìm thấy, .attrs sẽ trả về dic các thuộc tính
print("------------lấy các thuộc tính của thẻ p đầu tiên:", soup.p.attrs)

# do soup.p.attrs là dic, nên lấy theo key là 'id'
print("------------lấy thuộc tính id của thẻ p đầu tiên:", soup.p.attrs['id'])


print('------------tìm thẻ p đầu tiên:', soup.find('p'))
print('------------lấy tất cả các thẻ p:', soup.find_all('p'))

print('------------Lấy các bài viết')
# Tìm tất cả các thẻ div mà có thuộc tính data = 'tin_tuc'
list_all_post = soup.find_all('div', {'data': "tin_tuc"})
for v in list_all_post:
    print( v.a.text) # Lấy text của thẻ a trong bài viết
    print( v.div.p.text) # lấy phần nội dung của bài viết trong thẻ p, lưu ý đường dẫn tính từ thẻ div có data = 'tin_tuc'
    print()