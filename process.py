log_file = open("um-server-01.txt") #this is opening the file containing the information

#this is a function to call the sales reports
def sales_reports(log_file):
    #this is a loop that loops through the log file
    for line in log_file:
        line = line.rstrip()# rstrip is removing the white spaces on the right side of the line
        day = line[0:3] 
        if day == "Mon":#conditional saying to pull anything with the keyword "Mon"
            print(line)


sales_reports(log_file) #this is using the function above and calling the log_file to apply it
