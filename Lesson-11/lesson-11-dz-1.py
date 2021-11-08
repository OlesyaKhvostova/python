class MyDate:
    """ Date format (day-month-year)"""
    def __init__(self, value : str):
        self.value = value

    @classmethod
    def get_date_values(cls, mydate):
        values_lst = list(mydate.value.split('-'))
        output_prms = {'day':1,'month':1,'year':2000}

        if (len(values_lst) == 3):
            temp = list(map(int, values_lst))
            output_prms['day'] = temp[0]
            output_prms['month'] = temp[1]
            output_prms['year'] = temp[2]
        else:
            print(f'{mydate.value} неправльные параметры даты')
            return {}

        if (MyDate.check_params(output_prms)):
            return output_prms
        else:
            print(f'{mydate.value} неправльные параметры даты')

        return {}

    @staticmethod
    def check_params(params):
        if (params['day'] < 1 or params['day'] > 31):
            return False

        if (params['month'] < 1 or params['month'] > 12):
            return False

        if (params['year'] < 1):
            return False

        return True


date_temp = MyDate('24-10-1981')
out_params = MyDate.get_date_values(date_temp)
print(out_params)

date_temp = MyDate('35-10-1981')
out_params = MyDate.get_date_values(date_temp)
print(out_params)

date_temp = MyDate('20--5-1981')
out_params = MyDate.get_date_values(date_temp)
print(out_params)