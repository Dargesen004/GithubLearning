# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from _11_paskaitavenv2 import Project
#
# engine = create_engine("sqlite:///projects.db")
# Session = sessionmaker(bind = engine)
# session = Session()
# #Crud
# project1 = Project("statyba", 20006)
# project2 = Project("statyba2", 50000)
# project3 = Project("statyba3", 69000)
# project4 = Project("statyba4", 35000)
# # #sukuriame nauja irasa
# # session.add(project1)
# # # issaugome duombaze
# # session.commit()
# first_project = session.get(Project,1)
# # print(first_project)
# #
# #
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from _11_paskaitavenv2 import Project  # Make sure this file contains the Project class and Base setup

# Sukuriame duomenų bazės variklį
engine = create_engine("sqlite:///projects.db")

# Sukuriame sesijos klasę ir objektą
Session = sessionmaker(bind=engine)
session = Session()

# # CRUD operacijos – sukuriame projektų objektus
# project1 = Project("statyba", 20006)
# project2 = Project("statyba2", 50000)
# project3 = Project("statyba3", 69000)
# project4 = Project("statyba4", 35000)
#
# # Pridedame įrašus į sesiją
# session.add_all([project1, project2, project3, project4])
# # session.commit()  # Išsaugome pokyčius į duomenų bazę
#
# # Gauname įrašą su id=1
# first_project = session.get(Project, 1)
# print(first_project)

#Crud update
second_project = session.get(Project,1)
print(second_project)
print("\nAfter update:")
second_project.price = 99999
session.add(second_project)
session.commit()
second_project = session.get(Project,2)
print(second_project)