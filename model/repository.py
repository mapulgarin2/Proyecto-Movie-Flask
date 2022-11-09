from model.entity import Movie,Review


class MovieRepository:
    def insert(movie:Movie)->None:
        pass
    
    def findbyCode(code : str)->list:
        pass
    
    def findAll()->list:
        pass
    
class ReviewRepository:
    def insert(review: Review)->None:
        pass
    
    def findbyId(id : int)->list:
        pass
    
    def findAll()->list:
        pass
    pass

    def update(review : Review)->None:
        pass
    
    def delate(id : int)-> None:
        pass


        