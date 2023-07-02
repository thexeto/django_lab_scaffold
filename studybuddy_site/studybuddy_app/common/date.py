import datetime


def date_to_form(date):
    if date is None:
        return date
    date_form_format = '%Y-%m-%dT%H:%M'
    if type(date) == str:
        iso_t = datetime.datetime.strptime(date, date_form_format)
    else:
        iso_t = date.strftime(date_form_format)
    return iso_t


def date_from_form(date):
    if type(date) == str:
        date = datetime.datetime.fromisoformat(date)
        date = date.replace(tzinfo=datetime.timezone.utc)
        
    return date




  #  date_str = datetime.now().isoformat(' ', timespec='minutes')
  #      date_str = datetime.now().isoformat('T', timespec='minutes')
  #      self.assertEqual(date_str,"")
  #      date_str = '2023-07-27T02:10'
  #      a_date = datetime.fromisoformat(date_str)
  #      date_str_django = a_date.isoformat(' ', timespec='minutes')
  #      self.assertEqual(date_str_django, '2023-07-27 02:10')