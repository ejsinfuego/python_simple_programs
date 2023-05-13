#Python program to calculate student grades
def	inputmark () :
        #This function will get the input from the user
		print ( ' ENTER STUDENT ID :	')
		id=int (input ())
		print ( ' ENTER EXAM SCORE :	')
		exam=int (input ())
		print ( ' ENTER ALL TEST SCORES :	')
		mark1=int (input ())
		mark2=int (input ())
		mark3=int (input ())
		mark4=int (input ())
		mark5=int (input ())
		mark6=int (input ())
		mark7=int (input ())
		mark8=int (input ())
		mark9=int (input ())
		mark10=int (input ())
		#The formula on how to compute the average grade of the student
		sum= (mark1+mark2+mark3+mark4+mark5+mark6+mark7+mark8+mark9+mark10)
		avge=sum/10
		print ( ' TEST AVERAGE IS : '	+str (avge))
		print ( ' Final mark is: ', compute_mark(avge,exam))
		print ( ' Letter Grade is: ', getgrade (compute_mark (avge,exam)))
		print (print_Remark(getgrade(compute_mark(avge,exam))))
		return avge
def	compute_mark (avge,exam) :
    #This function will compute the final mark
		final_mark= avge+ 0.4 + exam
		return final_mark
def	getgrade (final_mark) :
    #This function will set the letter grade depends on the final mark
		if 95<=final_mark<=100:
			grade='A+'
		elif 90<=final_mark<=94:
			grade='A'
		elif 85<=final_mark<=89:
			grade='B+'
		elif 80<=final_mark<=84:
			grade='B'
		elif 75<=final_mark<=79:
			grade='C+'	
		elif 70<=final_mark<=74:
			grade='C'
		elif 65<=final_mark<=69:
			grade='D+'
		elif 90<=final_mark<=100:
			grade='D'
		else:
			grade='F'
		return grade
def	print_Remark (grade) :
    #This function will provide the remak based on letter grade
		if grade=='A+' :	
			print ( ' Remark : VERY EXCELLENT ' )
		elif grade=='A' :
			print ( ' Remark : EXCELLENT ' )
		elif grade=='B+' :
			print ( ' Remark : VERY GOOD ' )
		elif grade=='B' :
			print ( ' Remark : GOOD ' )
		elif grade=='C+' :
			print ( ' Remark : VERY SATISFACTORY ' )
		elif grade=='C' :
			print ( ' Remark : SATISFACTORY ' )
		elif grade=='D+' :
			print ( ' Remark : VERY FAIR ' )
		elif grade=='D' :
			print ( ' Remark : FAIR ' )
		elif grade=='F' :
			print ( ' Remark : POOR ' )

inputmark () #Calling the function to get the input from the user