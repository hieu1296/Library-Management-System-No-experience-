class Book:
    def __init__(self, id:int, title,author = None, PublicationDate=None, status = "Available") -> None:
        self.title = title 
        self.id = id
        self.author = author
        self.status = status # Available, borrowed, or reserved
        self.PublicationDate = PublicationDate

    
    def updatestatus(self, newstatus):
        self.status = newstatus

    def checkstatus(self):
        return self.status