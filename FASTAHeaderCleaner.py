#A quick script for taking an input FASTA file and replacing all " "
#(space) characters with hypens ("-"), and simply removing all square
#brackets.  Written because some tools seem to truncate FASTA headers
#at these characters and this can be a pain when trying to later
#determine where that sequence came from.

if __name__ == "__main__":
    #Stuff for file selection dialogue boxes:
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()

    #Get a FASTA file to open
    #Loop while a location hasn't been set
    gettingLocation = True
    while (gettingLocation == True):
        print("\nPlease choose an input file with FASTA sequences: ")
        #Get a file location, set as inputFASTALocation
        inputFASTALocation = filedialog.askopenfilename()
        #Try to open the file, if successful set as FASTAData
        try:
            inputFASTA = open(inputFASTALocation,"r")
            FASTAData = inputFASTA.read()
            gettingLocation = False
        #If opening the file fails alert the user and try again
        except IOError:
            print("Sorry, I'm unable to open that file location.")
    
    #Get a file location to save the output data
    gettingLocation = True
    #Get a file location, set as outputFASTALocation
    while (gettingLocation == True):
        print("\nPlease choose an output file location and file name: ")
        outputFileLocation = filedialog.asksaveasfilename()
        #Try to open the file, if successful set as "file"
        try:
            file = open(outputFileLocation,"w")
            gettingLocation = False
        #If opening the file fails alert the user and try again
        except IOError:
            print("Sorry, I'm unable to open that file location.")

    #Count the number of sequences in the input file by counting ">" 
    numberOfSeqs = FASTAData.count(">")
    print("There are " + str(numberOfSeqs) + " sequences in this file")

    #Split the input file into separate lines
    FASTAData = FASTAData.splitlines()

    with open(outputFileLocation, "a") as file:
        #For each line in the input file:
        for line in FASTAData:
            #Replace all spaces with hyphens
            newLine = line.replace(" ", "-")
            #Remove all square brackets
            newLine = line.replace("[", "")
            newLine = line.replace("]", "")
            #Write the line to the output file
            file.write(newLine)

    print("Done!")



