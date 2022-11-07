from datetime import datetime


def days_elapsed(date1, date2):
    """
    :param date1: 1st date to compare
    :param date2: 2nd date to compare
    :return: difference between date1 and date2
    """
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')

    return (date1_obj - date2_obj).days


if __name__ == "__main__":
	print(days_elapsed("2022-11-01", "2021-11-01"))
