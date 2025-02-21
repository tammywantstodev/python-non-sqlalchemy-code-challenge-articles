class Article:
    all=[]
    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
             self.author=author
        else:
            raise TypeError("author must be an instance of Author")
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("author must be an instance of Author")
        
       
    @property
    def title(self):
            return self._title
    @title.setter
    def title(self, title):
        if not hasattr(self, '_title'):
            if isinstance(title,str) and 5<=len(title)<=50:
                    self._title=title
            else:
                raise ValueError ("Title must be a string between 5 and 50 characters")


        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if not hasattr(self, '_name'):
            if isinstance(name, str) and len(name)>0:
                self._name=name
            else:
                raise ValueError ("Name must be a string greater than 0 characters")
    

    def articles(self):
            return [article for article in Article.all if article.author == self]

    def magazines(self):
            return list(set(article.magazine for article in self.articles()))


    def add_article(self, magazine, title):
        new_article=Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        categories = {article.magazine.category for article in self.articles()}
        return list(categories)



class Magazine:
    all=[]
    def __init__(self, name, category):
        self._name=None
        self._category=None
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<=len(name)<=16:
            self._name=name  
        Magazine.all.append(self)

    @property
    def category(self):
        return self._category 
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0<len(category):
            self._category=category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if not self.articles():
            return None
        
        author_article_count = {}
        
        for article in self.articles():
            author = article.author
            if isinstance(author, Author):  
                if author not in author_article_count:
                    author_article_count[author] = 0
                author_article_count[author] += 1
        
        contributing_authors = [author for author, count in author_article_count.items() if count > 2]
        
        if not contributing_authors:
            return None
        
        return contributing_authors

