import re

import dateparser
import pytz


def getTimeZoneName(date, timezone):
    # See if it's already a valid time zone name
    if timezone in pytz.all_timezones:
        return timezone

    # If it's a number value, then use the Etc/GMT code
    try:
        offset = int(timezone)
        if offset > 0:
            offset = '+' + str(offset)
        else:
            offset = str(offset)
        return 'Etc/GMT' + offset
    except ValueError:
        pass

    set_zones = set()

    # Try to match the timezone abbreviation to any time zone
    for name in pytz.all_timezones:
        tzone = pytz.timezone(name)

        for utcoffset, dstoffset, tzabbrev in getattr(tzone, '_transition_info',
                                                      [[None, None,
                                                        tzone.localize(dateparser.parse(date), is_dst=None).tzname()]]):
            if tzabbrev.upper() == timezone.upper():
                set_zones.add(name)

    return min(set_zones, key=len)


class TimezoneConverter():
    def __init__(self, date):
        self.original_tz_name = ""
        self.converted_tz_name = ""
        self.date = date

    def convertDate(self):
        converted_date = self.date

        if self.date is not None:

            # Separate the original and target TZs and date
            tz_Str = re.sub(r'[^A-Za-z /_]+', '', self.date).split()
            tz_Str = [word for word in tz_Str if word not in ["/"]]

            self.date = re.sub(r'[^0-9 /.:-]+', '', self.date)
            self.date = self.date[:-1].strip()

            original_tz_str = tz_Str[0]
            target_tz_str = tz_Str[-1] if len(tz_Str) > 1 else "UTC"

            # Convert tz strings to timezones
            original_timezone = pytz.timezone(getTimeZoneName(self.date, original_tz_str))
            target_timezone = pytz.timezone(getTimeZoneName(self.date, target_tz_str))

            # Get the timezones' abbreviation
            self.original_tz_name = original_timezone.localize(dateparser.parse(self.date), is_dst=None).tzname()
            self.converted_tz_name = target_timezone.localize(dateparser.parse(self.date), is_dst=None).tzname()

            # print(f'{self.date}__{original_timezone}::{original_tz_str}__{target_timezone}::{target_tz_str}__{self.original_tz_name}::{self.converted_tz_name}')

            converted_date = dateparser.parse(f'{self.date} {self.original_tz_name}')

            if converted_date is not None:
                converted_date = converted_date.astimezone(target_timezone)

        return converted_date
