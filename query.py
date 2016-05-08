"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corv_models = Model.query.filter(Model.name=='Corvette', Brand.name=='Chevrolet').all() 

# Get all models that are older than 1960.

older_models = Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.

newer_brands = Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".

cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

founded_brands = Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

all_brands = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded<1950)).all()

# Get any model whose brand_name is not Chevrolet.

model_not_chevy = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    #This produces a list of tuples, not sure how you want it to look in it's final state    
    model_year = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year==Model.year).all()


    #Realized the below took longer to do and would have to join it to the Brand class.
    #Also wasn't sure how you wanted the final result so I went with the above solution.
    # model_by_year = Model.query.filter(Model.year == Model.year).all()

    # for model in model_by_year:
    #     print model.name, model.brand_name
    # pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     brand_summary = db.session.query(Brand.name, Model.name)

     for brand in brand_summary:
        print brand

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

#Value is <flask_sqlalchemy.BaseQuery object at 0x103c4f910>
#Datatype is Class <class 'flask_sqlalchemy.BaseQuery'>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

#Association table is created to manage tables that have a many-to-many relationship. 
#This table only houses it's primary key and the foreign keys that help to associate 
#the other tables.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    search_brands = Brand.query.filter((Brand.name.like('%'+mystr+'%')) | (Brand.name==mystr)).all()
    return search_brands

def get_models_between(start_year, end_year):
    get_models = Model.query.filter(Model.year=>start_year, Model.year=<end+year).all()
    return get_models