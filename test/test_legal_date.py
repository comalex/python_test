import unittest
from ..legal_date import convert_date, fix_year_format


class LegalDateTest(unittest.TestCase):
    def test_convert_date(self):
        dataset = [
            ("1/2/3", "2001-02-03"),
            ("3/20/1", "2001-03-20"),
            ("3/20/2003", "2003-03-20"),
            ("3/20/1993", "1993-03-20"),
        ]
        for data in dataset:
            input_date, output_date = data
            self.assertEqual(convert_date(input_date), output_date)

    def test_convert_date_illegal(self):
        self.assertIn("is illegal", convert_date("20/20/3"))

    def test_fix_year(self):
        for data in ["03", "3", "2003", "003"]:
            self.assertEqual(fix_year_format(data), "2003")

    def test_earliest_possible_legal_date(self):
        """
            from "1/2/3" depends of date style is possible two correct date:
            "2003-03-01"
            "2001-02-03"
            correct one is the earliest
        """
        date = convert_date("1/2/3")
        posible_res = "2001-02-03"
        self.assertEqual(date, posible_res)

if __name__ == "__main__":
    unittest.main()
