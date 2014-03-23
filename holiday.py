#-*- coding: utf-8 -*-
import calendar
class Holiday:
	def __init__(self):
		pass

	def getHolidays(self, year, month):
		holidays = {}
		if year < 1948 or year == 1948 and month < 7:
			return holidays

		if month == 1:
			holidays[1] = "元日"
			if 1949 <= year <= 1999:
				holidays[15] = "成人の日"
			elif 2000 <= year:
				holidays[self.getNthWeekday(year, month, 2, 0)] = "成人の日"

		elif month == 2:
			if 1967 <= year:
				holidays[11] = "建国記念の日"

		elif month == 3:
			if year % 4 == 0:
				if year <= 1956:
					holidays[21] = "春分の日"
				elif year <= 2088:
					holidays[20] = "春分の日"
				elif year <= 2096:
					holidays[19] = "春分の日"
			elif year % 4 == 1:
				if year <= 1989:
					holidays[21] = "春分の日"
				elif year <= 2097:
					holidays[20] = "春分の日"
			elif year % 4 == 2:
				if year <= 2022:
					holidays[21] = "春分の日"
				elif year <= 2098:
					holidays[20] = "春分の日"
			elif year % 4 == 3:
				if year <= 2055:
					holidays[21] = "春分の日"
				elif year <= 2099:
					holidays[20] = "春分の日"
					
		elif month == 4:
			if year <= 1988:
				holidays[29] = "建国記念の日"
			elif 1989 <= year <= 2006:
				holidays[29] = "みどりの日"
			elif 2007 <= year:
				holidays[29] = "昭和の日"

		elif month == 5:
			holidays[3] = "憲法記念日"
			if 2007 <= year:
				holidays[4] = "みどりの日"
			holidays[5] = "こどもの日"

		elif month == 6:
			pass

		elif month == 7:
			if 1996 <= year <= 2002:
				holidays[20] = "海の日"
			elif 2003 <= year:
				holidays[self.getNthWeekday(year, month, 3, 0)] = "海の日"

		elif month == 8:
			pass

		elif month == 9:
			if 1966 <= year <= 2002:
				holidays[15] = "敬老の日"
			elif 2003 <= year:
				holidays[self.getNthWeekday(year, month, 3, 0)] = "敬老の日"
			if year % 4 == 0:
				if year <= 2008:
					holidays[23] = "秋分の日"
				elif year <= 2096:
					holidays[22] = "秋分の日"
			elif year % 4 == 1:
				if year <= 2041:
					holidays[23] = "秋分の日"
				elif year <= 2097:
					holidays[22] = "秋分の日"
			elif year % 4 == 2:
				if year <= 2074:
					holidays[23] = "秋分の日"
				elif year <= 2098:
					holidays[22] = "秋分の日"
			elif year % 4 == 3:
				if year <= 1979:
					holidays[24] = "秋分の日"
				elif year <= 2099:
					holidays[23] = "秋分の日"

		elif month == 10:
			if 1966 <= year <= 1999:
				holidays[10] = "体育の日"
			elif 2000 <= year:
				holidays[self.getNthWeekday(year, month, 2, 0)] = "体育の日"

		elif month == 11:
			holidays[3] = "文化の日"
			holidays[23] = "勤労感謝の日"

		elif month == 12:
			if 1989 <= year:
				holidays[23] = "天皇誕生日"

		for d, holiday_name in {key: val for key, val in holidays.items()}.items():
			if calendar.weekday(year, month, d) == 6:
				while 5 <= calendar.weekday(year, month, d) or d in holidays:
					d += 1
				holidays[d] = "{0} 振替休日".format(holiday_name)
				
		return holidays

	def getNthWeekday(self, year, month, nth, weekday):
		first_weekday, days = calendar.monthrange(year, month)
		count = 0
		for i in range(days):
			if first_weekday % 7 == weekday:
				count += 1
				if count == nth:
					return i + 1
			first_weekday += 1
		return 0
