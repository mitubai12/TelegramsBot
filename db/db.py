import aiosqlite
from db.queries import Queries

class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            async with conn.cursor() as cur:
                await cur.execute(Queries.CREATE_SURVEY_TABLE)
                await cur.execute(Queries.CREATE_MEALS_TABLE)
                await cur.execute(Queries.CREATE_CATEGORIES_TABLE)
                await cur.execute(Queries.POPULATE_CATEGORIES)
                await cur.execute(Queries.POPULATE_MEALS)
                await conn.commit()

    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query,params)
            await conn.commit()

    async def fetch(self, query: str, params: tuple = (), fetch_type: str = "all"):
        async with aiosqlite.connect(self.path) as conn:
            conn.row_factory = aiosqlite.Row
            data = await conn.execute(query, params)
            if fetch_type == "one":
                result = await data.fetchone()
                return dict(result)
            else:
                result = await data.fetchall()
                return [dict(row) for row in result]