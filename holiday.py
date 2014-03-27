#-*- coding: utf-8 -*-
import calendar
class Holiday:
	def __init__(self):
		self.holiday_list = {
			"gantan": "元日",
			"seijin": "成人の日",
			"kenkokukinen": "建国記念の日",
			"shunbun": "春分の日",
			"tennou": "天皇誕生日",
			"midori": "みどりの日",
			"showa": "昭和の日",
			"kenpou": "憲法記念日",
			"kodomo": "こどもの日",
			"umi": "海の日",
			"keirou": "敬老の日",
			"shubun": "秋分の日",
			"taiiku": "体育の日",
			"bunka": "文化の日",
			"kinroukansha": "勤労感謝の日",
		}

	def getHolidays(self, year, month):
		holidays = {}
		if year < 1948 or year == 1948 and month < 7 or 2100 <= year:
			return holidays

		if month == 1:
			holidays[1] = self.holiday_list["gantan"]
			if 1949 <= year <= 1999:
				holidays[15] = self.holiday_list["seijin"]
			elif 2000 <= year:
				holidays[self.getNthWeekday(year, month, 2, 0)] = self.holiday_list["seijin"]

		elif month == 2:
			if 1967 <= year:
				holidays[11] = self.holiday_list["kenkokukinen"]

		elif month == 3:
			if year % 4 == 0:
				if year <= 1956:
					holidays[21] = self.holiday_list["shunbun"]
				elif year <= 2088:
					holidays[20] = self.holiday_list["shunbun"]
				elif year <= 2096:
					holidays[19] = self.holiday_list["shunbun"]
			elif year % 4 == 1:
				if year <= 1989:
					holidays[21] = self.holiday_list["shunbun"]
				elif year <= 2097:
					holidays[20] = self.holiday_list["shunbun"]
			elif year % 4 == 2:
				if year <= 2022:
					holidays[21] = self.holiday_list["shunbun"]
				elif year <= 2098:
					holidays[20] = self.holiday_list["shunbun"]
			elif year % 4 == 3:
				if year <= 2055:
					holidays[21] = self.holiday_list["shunbun"]
				elif year <= 2099:
					holidays[20] = self.holiday_list["shunbun"]
					
		elif month == 4:
			if year <= 1988:
				holidays[29] = self.holiday_list["tennou"]
			elif 1989 <= year <= 2006:
				holidays[29] = self.holiday_list["midori"]
			elif 2007 <= year:
				holidays[29] = self.holiday_list["showa"]

		elif month == 5:
			holidays[3] = self.holiday_list["kenpou"]
			if 2007 <= year:
				holidays[4] = self.holiday_list["midori"]
			holidays[5] = self.holiday_list["kodomo"]

		elif month == 6:
			pass

		elif month == 7:
			if 1996 <= year <= 2002:
				holidays[20] = self.holiday_list["umi"]
			elif 2003 <= year:
				holidays[self.getNthWeekday(year, month, 3, 0)] = self.holiday_list["umi"]

		elif month == 8:
			pass

		elif month == 9:
			if 1966 <= year <= 2002:
				holidays[15] = self.holiday_list["keirou"]
			elif 2003 <= year:
				holidays[self.getNthWeekday(year, month, 3, 0)] = self.holiday_list["keirou"]
			if year % 4 == 0:
				if year <= 2008:
					holidays[23] = self.holiday_list["shubun"]
				elif year <= 2096:
					holidays[22] = self.holiday_list["shubun"]
			elif year % 4 == 1:
				if year <= 2041:
					holidays[23] = self.holiday_list["shubun"]
				elif year <= 2097:
					holidays[22] = self.holiday_list["shubun"]
			elif year % 4 == 2:
				if year <= 2074:
					holidays[23] = self.holiday_list["shubun"]
				elif year <= 2098:
					holidays[22] = self.holiday_list["shubun"]
			elif year % 4 == 3:
				if year <= 1979:
					holidays[24] = self.holiday_list["shubun"]
				elif year <= 2099:
					holidays[23] = self.holiday_list["shubun"]

		elif month == 10:
			if 1966 <= year <= 1999:
				holidays[10] = self.holiday_list["taiiku"]
			elif 2000 <= year:
				holidays[self.getNthWeekday(year, month, 2, 0)] = self.holiday_list["taiiku"]

		elif month == 11:
			holidays[3] = self.holiday_list["bunka"]
			holidays[23] = self.holiday_list["kinroukansha"]

		elif month == 12:
			if 1989 <= year:
				holidays[23] = self.holiday_list["tennou"]

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
	
	def getHolidayName(self, year, month, day):
		return self.getHolidays(year, month).get(day, None)

