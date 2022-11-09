class Movie:
    def __init__(self,code,name,image=None,year=None)->None:
        self.code = code
        self.name = name
        self.image = image
        self.year = year
        
class Review:
    def __init__(self,name,email,description,rating,movie_code,id=None) -> None:
        self.id = id
        self.name =name
        self.email = email
        self.description = description
        self.rating = rating
        
        pass   
    
                 
    