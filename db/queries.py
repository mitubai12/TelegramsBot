class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact INTEGER,
            visit_date TEXT,
            rate_dish TEXT,
            rate_cleanles TEXT,
            comments TEXT
        )
    """

    CREATE_CATEGORIES_TABLE = """
           CREATE TABLE IF NOT EXISTS categories (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT
           )
       """
    CREATE_MEALS_TABLE = """
           CREATE TABLE IF NOT EXISTS meals (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               price INTEGER,
               image TEXT,
               category_id INTEGER,
               FOREIGN KEY (category_id) REFERENCES categories(id)
           ) 
       """
    POPULATE_CATEGORIES = """
           INSERT INTO categories (name)
           VALUES ("Суши"),
           ("Пицца")
       """
    POPULATE_MEALS = """
           INSERT INTO meals (name, price, image, category_id)
           VALUES ("Филадельфия", 1500, "img/sushi.jpeg", 1),
           ("Пеперонни", 750, "img/pizza.jpeg", 2),
           ("Пицца 30 см", 500, "img/pizza.jpeg", 2),
           ("Суши другой", 1350, "img/sushi.jpeg", 1)
       """