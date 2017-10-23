from datetime import datetime
import logging


logger = logging.getLogger(__name__)


def fix_year_format(year):
    """
        Input - 03, 3, 003, 2003
        Output - 2003
    """
    if len(year) == 4:
        return str(year)
    return "2" + year.zfill(4)[1:]


def american_date_validator(date_elements):
    year, month, day = date_elements
    date_string = "{year}/{month}/{day}".format(year=fix_year_format(year), month=month, day=day)
    return datetime.strptime(date_string, '%Y/%m/%d')


def all_world_date_validator(date_elements):
    day, month, year = date_elements
    date_string = "{month}/{day}/{year}".format(year=fix_year_format(year), month=month, day=day)
    return datetime.strptime(date_string, '%d/%m/%Y')


def convert_date(input_string):
    date_elements = input_string.split("/")

    dates = []
    for date_validator in [american_date_validator, all_world_date_validator]:
        try:
            date = date_validator(date_elements)
            dates.append(date)
        except ValueError as e:
            # logger.error(e, exc_info=True)
            pass

    if not dates:
        return "{} - is illegal".format(input_string)

    earliest_date = min(dates)
    return earliest_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    """
        1/2/3 => 2001-02-3
        3/20/1 => 2001-03-20
    """
    print("1/2/3", "->", convert_date("1/2/3"))
    print("3/20/1", "->", convert_date("3/20/1"))
