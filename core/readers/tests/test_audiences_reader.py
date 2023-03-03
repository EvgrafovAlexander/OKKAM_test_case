# stdlib
import datetime
import unittest

# project
from common import db_common
from readers import audiences_reader


class TestAudiencesReader(unittest.TestCase):
    @classmethod
    async def setUpClass(cls) -> None:
        cls.date = datetime.date(1900, 1, 1)
        insert_sql = """
            insert into audiences
            (
                date,
                respondent,
                sex,
                age,
                weight
            )
            values
            (
                :date,
                :respondent,
                :sex,
                :age,
                :weight
            )
        """

        cls.insert_data = [
            {
                "respondent": -1,
                "date": cls.date,
                "sex": -0,
                "age": 100,
                "weight": 3,
            },
            {
                "respondent": -2,
                "date": cls.date,
                "sex": -0,
                "age": 100,
                "weight": 1,
            },
            {
                "respondent": -1,
                "date": cls.date,
                "sex": -1,
                "age": 101,
                "weight": 3,
            },
            {
                "respondent": -5,
                "date": cls.date,
                "sex": -1,
                "age": 200,
                "weight": 3,
            },
            {
                "respondent": -1,
                "date": cls.date,
                "sex": -2,
                "age": 102,
                "weight": 1,
            },
            {
                "respondent": -2,
                "date": cls.date,
                "sex": -2,
                "age": 103,
                "weight": 3,
            },
        ]

        await db_common.execute_multiple([(insert_sql, cls.insert_data)])

    @classmethod
    async def tearDownClass(cls) -> None:
        delete_sql = "delete from audiences au where au.date = :date"
        await db_common.execute_multiple([(delete_sql, cls.insert_data)])

    async def test_get_percent(self):
        expected = [{"percent": 75.0}]
        result = await audiences_reader.get_percent_data("Age = 100", "Age = 101")
        self.assertListEqual(result, expected)

    async def test_get_percent_with_identical_audiences(self):
        expected = [{"percent": 100.0}]
        result = await audiences_reader.get_percent_data("Age = 100", "Age = 100")
        self.assertListEqual(result, expected)

    async def test_get_percent_with_no_intersections(self):
        expected = [{"percent": 0.0}]
        result = await audiences_reader.get_percent_data("Age = 100", "Age = 200")
        self.assertListEqual(result, expected)

    async def test_get_percent_where_2au_in_1au(self):
        expected = [{"percent": 25.0}]
        result = await audiences_reader.get_percent_data("Age in (102, 103)", "Age = 102")
        self.assertListEqual(result, expected)

    async def test_get_percent_where_1au_in_2au(self):
        expected = [{"percent": 100.0}]
        result = await audiences_reader.get_percent_data("Age = 102", "Age in (102, 103)")
        self.assertListEqual(result, expected)

    async def test_get_percent_not_exist_group(self):
        expected = [{"percent": 100.0}]
        result = await audiences_reader.get_percent_data("Age = 130", "Age = 140")
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
