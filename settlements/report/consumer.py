from settlements.report.DayReport import DayReport
from settlements.report.WeekReport import WeekReport
from settlements.report.api import DayResult,WeekResult

class Consumer(object):

    def __init__(self, begin_date, end_date):
        self.begin_date = begin_date
        self.end_date = end_date

    def consumer(self):
        if self.begin_date == self.end_date:
            DayReport().insert_data(self.begin_date)
            DayResult().get_data(self.begin_date)
        else:
            WeekReport().get_master_data(begin_date=self.begin_date, end_date=self.end_date)
            WeekResult().get_data(begin_date=self.begin_date,end_date=self.end_date)


if __name__ == '__main__':
    pass
    # Consumer(begin_date='2019-09-01',end_date='2019-09-01').consumer()
    # Consumer(begin_date='2019-09-02',end_date='2019-09-02').consumer()
    # DayResult().get_data('2019-10-
    # Consumer(begin_date='2019-09-01', end_date='2019-09-15').consumer()
    # Consumer(begin_date='2019-09-16', end_date='2019-09-30').consumer()
    # Consumer(begin_date='2019-10-01', end_date='2019-10-15').consumer()
    # Consumer(begin_date='2019-10-16', end_date='2019-10-31').consumer()
    # Consumer(begin_date='2019-11-01', end_date='2019-11-15').consumer()
    # Consumer(begin_date='2019-11-16', end_date='2019-10-31').consumer()
    # Consumer(begin_date='2019-10-16', end_date='2019-10-31').consumer()
    # Consumer(begin_date='2019-10-16', end_date='2019-10-31').consumer()
    #
    # Consumer(begin_date='2019-10-16', end_date='2019-10-31').consumer()
    # Consumer(begin_date='2019-10-16', end_date='2019-10-31').consumer()
    # date = '2019-09-01'
    import datetime
    for i in range(80):
        begin_date = datetime.datetime.strptime('2019-09-01','%Y-%m-%d') + datetime.timedelta(days=i)
        begin_date = datetime.datetime.strftime(begin_date,'%Y-%m-%d')
        Consumer(begin_date=begin_date,end_date=begin_date).consumer()




# other_config = {
#     '10204': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr': 'Y'},
#               'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45,'use_master_mdr': 'Y'}
#               },
#     '10186': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr': 'N'},
#               'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr': 'N'}
#               },
#     '10209': {'wechat': {'mdr_agency': 1.65, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr': 'N'},
#               'alipay': {'mdr_agency': 1.8, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr': 'N'}
#               },
#     '10203': {'wechat': {'mdr_agency': 1.65, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr': 'N'},
#               'alipay': {'mdr_agency': 1.8, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr': 'N'}
#               },
#     '0':     {'wechat': {'mdr_agency': 1.8, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr': 'N'},
#               'alipay': {'mdr_agency': 1.8, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr': 'N'}
#               },
# }