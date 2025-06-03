#Task 1
class MovieTracker:
    count_of_movies = 0

    def __init__(self,title,director,year):
        self.title = title
        self.director = director
        self.year = year
        MovieTracker.count_of_movies += 1

    def info(self):
        return f"The Movie: {self.title}, The Director: {self.director}, And The Year: {self.year}"
    
    @classmethod
    def movie_counter(cls):
        return cls.count_of_movies
    
    @staticmethod
    def form_for_entertaiment():
        return True
    
movie1 = MovieTracker("Batman", "Tom Holland", 2001)
movie2 = MovieTracker("Spider-Man", "Tommie Magguare", 1999)

print(movie1.info())
print(movie2.info())

print(MovieTracker.movie_counter())
print(MovieTracker.form_for_entertaiment())


#Task 2
class Recipe:
    count_food = 0

    def __init__(self, name, ingridients, prep_time):
        self.name = name
        self.ingredients = ingridients
        self.prep_time = prep_time
        Recipe.count_food += 1

    def information(self):
        return f"Name of food: {self.name}, ingredients: {self.ingredients} and preparation time: {self.prep_time}"

    @classmethod
    def food_counter(cls):
        return cls.count_food
    
    @staticmethod
    def are_edible():
        return True

food = Recipe("Plov", "Rice,Carrot,Oil, etc.", "2 Hours")

print(food.information())

print(Recipe.food_counter())
print(Recipe.are_edible())


#Task3
class Employee:
    number_employees = 0

    def __init__(self, first_name, last_name, position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        Employee.number_employees += 1
    
    def info_about_employee(self):
        return f"{self.last_name} {self.first_name}, Position: {self.position}"

    @classmethod
    def employee_counter(cls):
        return f"Number of employees in company: {cls.number_employees}"
    
    @staticmethod
    def slogan():
        return "Our Slogan: 'We Code The Future'"
    
employee1 = Employee("Azimjon", "Sobirov", "Software Developer")
employee2 = Employee("Ramziddin", "Makhmudov", "Frontend Developer")

print(employee1.info_about_employee())
print(employee2.info_about_employee())

print(Employee.employee_counter())
print(Employee.slogan())