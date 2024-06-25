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