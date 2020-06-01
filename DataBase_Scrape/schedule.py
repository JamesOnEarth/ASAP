def schedule_day(meetings):
    last_end = -1
    for end,start in sorted( (end,start) for start,end in meetings ):
        if start >= last_end:
            last_end = end
        elif start < last_end:
        	return False

    return True

def checkConflict(meetings,optional):
    last_end = -1
    joint = meetings + optional
    for end,start in sorted( (end,start) for start,end in joint ):
        if start >= last_end:
            last_end = end
        elif start < last_end:
        	return True

    return False


def schedule(must_haves, want_to_haves):
	result = False;
	schedules = []
	for section1 in must_haves[0]:
		for section2 in must_haves[1]:
			for section3 in must_haves[2]:
				for section4 in must_haves[3]:
					for section5 in must_haves[4]:
						for section6 in must_haves[5]:
							for section7 in must_haves[6]:
								for section8 in must_haves[7]:
									monday = []
									tuesday = []
									wednesday = []
									thursday = []
									friday = []
									saturday = []
									sunday = []
									if(section1 != None):
										for meetings in section1['meetings']:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section2 != None):
										for meetings in section2['meetings']:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section3 != None):
										for meetings in section3["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section4 != None):
										for meetings in section4["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section5 != None):
										for meetings in section5["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section6 != None):
										for meetings in section6["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section7 != None):
										for meetings in section7["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
									if(section8 != None):
										for meetings in section8["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])

									if(schedule_day(monday) == True and schedule_day(tuesday) == True and schedule_day(wednesday) == True and schedule_day(thursday) == True and schedule_day(friday) == True and schedule_day(saturday) == True and schedule_day(sunday) == True):
										result = True;

										for optional1 in want_to_haves[0]:
											for optional2 in want_to_haves[1]:
												for optional3 in want_to_haves[2]:
													for optional4 in want_to_haves[3]:
														for optional5 in want_to_haves[4]:
															for optional6 in want_to_haves[5]:
																for optional7 in want_to_haves[6]:
																	optionalMonday = []
																	optionalTuesday = []
																	optionalWednesday = []
																	optionalThursday = []
																	optionalFriday = []
																	optionalSaturday = []
																	optionalSunday = []

																	if(optional1 != None):
																		for optMeetings in optional1["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																	
																	if(optional2 != None):
																		for optMeetings in optional2["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])

																	if(optional3 != None):
																		for optMeetings in optional3["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])

																	if(optional4 != None):
																		for optMeetings in optional4["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])

																	if(optional5 != None):
																		for optMeetings in optional5["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])

																	if(optional6 != None):
																		for optMeetings in optional6["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])

																	if(optional7 != None):
																		for optMeetings in optional7["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(meetings1[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(meetings1[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])

																	if(checkConflict(monday,optionalMonday) == False and checkConflict(tuesday,optionalTuesday) == False and checkConflict(wednesday,optionalWednesday) == False and checkConflict(thursday,optionalThursday) == False and checkConflict(friday,optionalFriday) == False and checkConflict(saturday,optionalSaturday) == False and checkConflict(sunday,optionalSunday) == False):
																		schedule = []
																		if(section1 != None):
																			schedule.append(section1)
																		if(section2 != None):
																			schedule.append(section2)
																		if(section3 != None):
																			schedule.append(section3)
																		if(section4 != None):
																			schedule.append(section4)
																		if(section5 != None):
																			schedule.append(section5)
																		if(section6 != None):
																			schedule.append(section6)
																		if(section7 != None):
																			schedule.append(section7)
																		if(section8 != None):
																			schedule.append(section8)
																		if(optional1 != None):
																			schedule.append(optional1)
																		if(optional2 != None):
																			schedule.append(optional2)
																		if(optional3 != None):
																			schedule.append(optional3)
																		if(optional4 != None):
																			schedule.append(optional4)
																		if(optional5 != None):
																			schedule.append(optional5)
																		if(optional6 != None):
																			schedule.append(optional6)
																		if(optional7 != None):
																			schedule.append(optional7)
																		schedules.append(schedule)

	
	if(result == True):
		return(schedules)
	else:
		return(schedules)

def generateSchedule(must_haves,want_to_haves,preferences):
	tempMustHaves = must_haves
	tempWantHaves = want_to_haves
	while(len(tempMustHaves) < 8):
		tempMustHaves.append([None])
	for i in want_to_haves:
		i.append(None)
	while(len(tempWantHaves) < 7):
		tempWantHaves.append([None])
	schedules = schedule(tempMustHaves, tempWantHaves)
	return schedules[0]

def main():
	# Must-takes/Personal Events
	# 1.CSE 120 TUTH 8:00-9:20 TH 10:00-10:50 @@@
	# 2.CSE 141 MWF 10:00-10:50 W 11:00-11:50 @@@
	# 3.CSE 141 TUTH 3:30-4:50 TU 2:00-2:50
	# 4.CSE 141L M 3:00-3:50 W 3:00-3:50 @@@
	# 5.CSE 141L M 4:00-4:50 W 4:00-4:50 @@@
	# 6.CSE 110 TUTH 2:00-3:20 W 9:00-11:50
	# 7.CSE 110 TUTH 2:00-3:20 W 9:00-11:50
	# 8.CSE 110 TUTH 2:00-3:20 W 9:00-11:50
	# 9.CSE 110 TUTH 2:00-3:20 W 12:00-2:50 @@@
	# 10.CSE 110 TUTH 2:00-3:20 W 12:00-2:50 @@

	# Want-to-takes
	# 11. ECE 107 TUTH 8:00-9:20 F 11:00-11:50
	# 12. CSE 130 MWF 4:00-4:50 TH 5:00-5:50 @@@
	# 13. CSE 111 MWF 4:00-4:50 TH 5:00-5:50


	#Start time, end time, index
	must_takes=[]
	#must_takes.append([{"id":1,"meetings":[["TU",80000,92000],["TH",80000,92000],["TH",100000,105000]]}])
	#must_takes.append([{"id":2,"meetings":[["M",100000,105000],["W",100000,105000],["W",110000,115000],["F",100000,105000]]},{"id":3,"meetings":[["TU",153000,165000],["TU",140000,145000],["TH",153000,165000]]}])
	#must_takes.append([{"id":4,"meetings":[["M",150000,155000],["W",150000,155000]]},{"id":5,"meetings":[["M",160000,165000],["W",160000,165000]]}])
	#must_takes.append([{"id":6,"meetings":[["TU",140000,152000],["TH",140000,152000],["W",90000,115000]],"finals":["M",150000,180000]},{"id":7,"meetings":[["TU",140000,152000],["TH",140000,152000],["W",90000,115000]],"finals":["M",150000,180000]},{"id":8,"meetings":[["TU",140000,152000],["TH",140000,152000],["W",90000,115000]],"finals":["M",150000,180000]},{"id":9,"meetings":[["TU",140000,152000],["TH",140000,152000],["W",120000,145000]],"finals":["M",150000,180000]},{"id":10,"meetings":[["TU",140000,152000],["TH",140000,152000],["W",120000,145000]],"finals":["M",150000,180000]}])
	must_takes.append([{'id': 'personal event', 'meetings': [['TU', 900, 1000], ['TH', 900, 1000]], 'finals': '', 'midterms': ''}])
	must_takes.append([{'meetings': [['TU', 1100, 1220], ['TH',1100, 1220], ['M', 1100, 1150]], 'finals': ['W', 1130, 1429], 'midterms': [], 'LE id': '016900', 'id': '016901'}]);
	must_takes.append([None]);
	must_takes.append([None]);
	must_takes.append([None]);
	must_takes.append([None]);
	must_takes.append([None]);
	must_takes.append([None]);

	want_to_takes=[]
	#want_to_takes.append([{"id":11,"meetings":[["TU",80000,92000],["TH",80000,92000],["F",110000,115000]]},None])
	#want_to_takes.append([{"id":12,"meetings":[["M",160000,165000],["W",160000,165000],["F",160000,165000],["TH",170000,175000]]},None])
	#want_to_takes.append([{"id":13,"meetings":[["M",160000,165000],["W",160000,165000],["F",160000,165000],["TH",170000,175000]]},None]);
	want_to_takes.append([None]);
	want_to_takes.append([None]);
	want_to_takes.append([None]);
	want_to_takes.append([None]);
	want_to_takes.append([None]);
	want_to_takes.append([None]);
	want_to_takes.append([None]);


	schedules = generateSchedule(must_takes,want_to_takes,[])
	print(schedules)
	#max = 0
	#for i in schedules:
#		if len(i) > max:
#			max = len(i)
#
#	final_schedules = []
#	for i in schedules:
#		if len(i) == max:
#			final_schedules.append(i)

#	print(final_schedules)

if __name__ == '__main__':
	main()