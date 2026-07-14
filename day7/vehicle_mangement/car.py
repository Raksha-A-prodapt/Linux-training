from exception import OwnerAlreadyExistsError
class Car:
  def __init__(self, brand, model, year,owner=None):
    self.brand=brand
    self.model=model
    self.year=year
    self.__owner=owner

  def start_engine(self):
    print(f"The engine of the {self.brand} {self.model} is starting")

  def show_info(self):
    print(f"Car Info: {self.year} {self.brand} {self.model}")
 
  def get_owner(self):
    return self.__owner
  def set_owner(self,owner):
     if not self.__owner:
        self.__owner=owner
     else: 
        #print(f"Car is already owned by {self.__owner}, you can't chnage")
        raise OwnerAlreadyExistsError(self.__owner)
