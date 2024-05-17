import scrapy

class BookSpider(scrapy.Spider):
    name = "books"
    book_count = 1
    page_count =0
    f = open("cok-satanlar.txt","a",encoding="UTF-8")
    
    
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&page=1"
    ]


    def parse(self,response):
        for book in response.css("div.product-cr"):
            book_name = book.css("div.name.ellipsis a span::text").get()
            publisher_name = book.css("div.publisher span a span::text").get()
            author = book.css("div.author span a span::text").get()
        
        
            self.f.write("*************************************\n")
            self.f.write(f"{self.book_count}.\n")
            self.f.write(f"Book: {book_name}\n")
            self.f.write(f"Publisher: {publisher_name}\n")
            self.f.write(f"Author: {author}\n")
            self.book_count +=1

        next_page= response.css("a.next::attr(href)").get()
        self.page_count +=1
        
        if next_page is not None and self.page_count <5:
            yield response.follow(next_page,callback = self.parse)
        else:
            self.f.close()



