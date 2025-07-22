# File Title: Date Format Converter
# Feature: Change date from one format to another.

print("___Date Format Converter___")

formatMenu = """
\t SELECT INPUT FORMAT
NOTE: Do not put only one number for month or day
You can select the separator of the month, day, year for customizable format.

1. Day-Month-Year (Customizable) -> Separate with a space
2. Month-Day-Year (Customizable) -> Separate with a space
3. Year-Month-Day (Customizable) -> Separate with a space
4. Mon D, Year (Dec 31, 2025) -> Separate with DOUBLE space
5. Month D, Year (December 31, 2025) -> Separate with DOUBLE space
"""

Month = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
shortMonth = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

try: 
    print(formatMenu)
    inputFormat = input("Enter the input format in number: ")
    inputText = input("Enter the date (separated each date with double space): ")
    
    print(formatMenu)
    outputFormat = input("Enter the output format in number: ")
    List = []
    
    if (inputFormat == "4" or inputFormat == "5"):
        List = inputText.split("  ")
    else:
        List = inputText.split(" ")
    dateList = []
     
    # separators = r"/- _.,~"
    for i in range(len(List)):
        date = List[i]
        date = date.replace(",", " ").replace(".", " ").replace("/", " ").replace("-", " ").replace("~", " ").replace("_", " ").replace("  ", " ")
        dateList.append(date.split(" "))
    # Change all input date to DMY format
    if (inputFormat == outputFormat):
        for date in dateList:
            print(date)
    else:
        if (inputFormat == "2"): # MDY
            for i in range(len(dateList)):
                temp = dateList[i][0] #month
                dateList[i][0] = dateList[i][1]
                dateList[i][1] = temp
        elif (inputFormat == "3"): #YMD
            for i in range(len(dateList)):
                temp = dateList[i][0] #year
                dateList[i][0] = dateList[i][2]
                dateList[i][2] = temp
        elif (inputFormat == "4"): # Mon d, yyyy
            for i in range(len(dateList)):
                month = dateList[i][0]
                mon = shortMonth.get(month)
                day = dateList[i][1]
                dateList[i][0] = day
                dateList[i][1] = mon
        elif (inputFormat == "5"): # Month d, yyyy
            for i in range (len(dateList)):
                month = dateList[i][0] 
                mon = shortMonth.get(month[0:3])
                day = dateList[i][1]
                dateList[i][0] = day
                dateList[i][1] = mon
        
        # output
        if (outputFormat == "2"): # DMY -> MDY
            for i in range(len(dateList)):
                month = dateList[i][1]
                dateList[i][1] = dateList[i][0]
                dateList[i][0] = month
        elif (outputFormat == "3"): #DMY -> YMD
            for i in range(len(dateList)):
                day = dateList[i][0]
                year = dateList[i][2]
                dateList[i][0] = year
                dateList[i][2] = day
        elif (outputFormat == "4"):  # DMY -> MMM d, yyy
            for i in range(len(dateList)):
                month = dateList[i][1]
                mon = Month.get(month)[0:3]
                day = dateList[i][0]
                dateList[i][0] = mon
                dateList[i][1] = day
        elif (outputFormat == "5"): #DMY -> MMMMM d, yyyy
            for i in range(len(dateList)):
                month = dateList[i][1]
                mon = Month.get(month)
                day = dateList[i][0]
                dateList[i][0] = mon
                dateList[i][1] = day
        
        if ("1" <= outputFormat <= "3"):
            separator = input("Enter the separator: ")
            for i in range(len(dateList)):
                print("{}{}{}{}{}".format(dateList[i][0], separator, dateList[i][1], separator, dateList[i][2]))
        else:
            for i in range(len(dateList)):
                print("{} {}, {}".format(dateList[i][0], dateList[i][1], dateList[i][2]))
except:
    print("Sorry, error appears!")
    
    
    
        
            
        