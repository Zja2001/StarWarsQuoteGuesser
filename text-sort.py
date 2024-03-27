def output_quotes_from_html(filenames: list[str]):
    """parse each HTML file in'filesnames' and write thier quotes to '.quotes' files """
    #open each transcript files
    for filename in filenames: 
        lines: list[str]
        with open(filename, "r", encoding="utf-8") as file:
            #get a list of each line in the file
            lines = file.readlines()
        # filter out lines that have span HTML tags in them 
        lines= [line 
                for line 
                in lines 
                if "<" not in line
                and "style=" not in line]
        # iterate over the lines (this is equivilant 
        # to for (int i = 0; ...) in other languages)
        for i in range (len(lines) - 1):
            # if the is no colon in the next line, and 
            #then the next line is a continuation of 
            # the current quote, so that the quote is all on one 
            # line
            if ":" not in lines[i+1]:
                lines[i] = lines[i].replace("\n", " ")
        # makes the list of lines 
        # into one big string
        lines = "".join(lines)
        # get list of each line
        # into one big string 
        lines = lines.splitlines()
        #filter out lines that dont
        # have a colon in them
        lines = [line for line in lines if ":" in line]
        #witr the quotes out to a file
        with open(filename.split(".")[0] + ".quotes", "w+", encoding = "utf-8") as out_file:
            for line in lines:
                out_file.write(f"{line}\n")

output_quotes_from_html(["A-New-Hope.html"])