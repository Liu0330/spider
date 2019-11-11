from lxml import etree

# str 类型的数据
books = '''
<?xml version="1.0" encoding="utf-8"?>
<bookstore> 
  <book category="cooking"> 
    <title lang="en">Everyday Italian</title>  
    <author>Giada De Laurentiis</author>  
    <year>2005</year>  
    <price>30.00</price> 
  </book>  
  <book category="children"> 
    <title lang="en">Harry Potter</title>  
    <author>J K. Rowling</author>  
    <year>2005</year>  
    <price>29.99</price> 
  </book>  
  <book category="web"> 
    <title lang="en">XQuery Kick Start</title>  
    <author>James McGovern</author>  
    <author>Per Bothner</author>  
    <author>Kurt Cagle</author>  
    <author>James Linn</author>  
    <author>Vaidyanathan Nagarajan</author>  
    <year>2003</year>  
    <price>50</price> 
  </book> 
  <book category="web1" cover="paperback"> 
    <title lang="en">Learning XML</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>39.95</price> 
  </book> 
    <book category="web2" cover="paperback"> 
    <title lang="en">Learning XML</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>40</price> 
  </book> 
    <book category="web3" cover="paperback"> 
    <title lang="en">Learning XML</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>39.95</price> 
  </book> 
</bookstore>
'''

if __name__ == '__main__':
    html = etree.HTML(books)
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
    # result = html.xpath('/html/body/bookstore/book/@category')
    # print(result)
    # //不论位置，找到所有
    # print(html.xpath('//book/@category'))
    # books = html.xpath('//book')
    # print('第一本书，当前路径，查询',books[0].xpath('./year/text()'))
    # # 第一本书
    # print('第一本书，//查询所有',books[0].xpath('..//year/text()'))

    # xpath索引从1开始
    # print(html.xpath('//book[position() <= 3]/title/text()'))

    # print(html.xpath('//book[@cover="paperback"]/title/text()'))
    # print(html.xpath('//book[@cover="paperback"][@category="web2"]/title/text()'))
    # print(html.xpath('//book[contains(@category,"web")][@cover="paperback"]/@category'))
    # print(html.xpath('//book|//title'))
    # print(html.xpath('//@*'))
    print(html.xpath('//book[price mod 2 = 0]/title/text()'))
    # 根据位置进行查询：position() last()