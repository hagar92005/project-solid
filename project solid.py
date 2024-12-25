
from abc import ABC, abstractmethod

# Single Responsibility Principle (SRP)
class Student:
    def init(self, student_id, name):
        self.student_id = student_id
        self.name = name

# Open/Closed Principle (OCP)
class Service(ABC):
    @abstractmethod
    def serve(self):
        pass

class CafeteriaService(Service):
    def serve(self):
        print("Serving food ")

class LibraryService(Service):
    def serve(self):
        print("Providing books on course material")

# Liskov Substitution Principle (LSP)
class Person(ABC):
    def init(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class Student(Person):
    def init(self, name, student_id):
        super().init(name)
        self.student_id = student_id
    
    def get_role(self):
        return "Student"

class Teacher(Person):
    def init(self, name, department):
        super().init(name)
        self.department = department
    
    def get_role(self):
        return "Prof"

# Interface Segregation Principle (ISP)
class Enrollable(ABC):
    @abstractmethod
    def enroll(self, course):
        pass

class Serviceable(ABC):
    @abstractmethod
    def request_service(self, service):
        pass

class AcademicStudent( Enrollable, Serviceable):
    
    def enroll(self, course):
        print(f"Student {self.name} enrolled in course {course}")

    def request_service(self, service):
        print(f"Student {self.name} requested {service.class.name}")

# Dependency Inversion Principle (DIP)
class University(ABC):
    def init(self):
        self.students = []
        self.services = []
        
        @abstractmethod
        def add_student(self, student):
            pass
        @abstractmethod 
        def add_service(self, service):
            pass
        @abstractmethod 
        def provide_services(self):
            pass
class UniversityImpl(University):
    def add_student(self, student): 
        print(f"Added student {student.name}")
        self.students.append(student) 
    def add_service(self, service):
        print(f"Added service {service.class.name}") 
        self.services.append(service) 
    def provide_services(self):
        for service in self.services: 
            service.serve()