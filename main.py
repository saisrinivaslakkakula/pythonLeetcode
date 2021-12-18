import csv
import json
import sys


# def main():
#     args = sys.argv[1:]
#
#     if args[len(args) - 2][-4:] == '.txt':


def main():
    args = sys.argv[1:]
    NFLDict = {}
    tempList = []

    # -c -v -x
    file_name = 'inputFile.txt'
    file_type = args[len(args) - 1]

    if 1:
        file_name_copy = file_name[0:-5]
        if file_type == '-c':
            print("Converting " + file_name + " to csv.")
            with open(file_name, 'r') as textFile:
                txtReader = csv.reader(textFile, delimiter='\t')
                with open(file_name_copy + ".csv", 'w', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    for r in txtReader:
                        # writer.writerow(i.split(' '))
                        writer.writerow(r)
        if file_type == '-j':
            print("Converting " + file_name + " to json.")
            with open(file_name, 'r') as textFile:
                txtReader = csv.reader(textFile, delimiter='\t')
                with open(file_name_copy + ".json", 'w') as fh:
                    next(txtReader)
                    for i in txtReader:
                        tempList = [{"Player": i[1], "Age": i[2]}]
                        testDict = {i[0]: tempList}

                        # add all dicts into 1
                        if i[0] in NFLDict:
                            NFLDict[i[0]].append(tempList)
                        else:
                            NFLDict.update(testDict)
                    json.dump(NFLDict, fh)
        if file_type == '-x':
            print("Converting " + file_name + " to xml.")
            with open(file_name, 'r') as textFile:
                txtReader = csv.reader(textFile, delimiter='\t')
                data = []
                temp = []
                next(txtReader)
                with open(file_name_copy + ".xml", 'w') as fh:
                    for i in txtReader:
                        fh.write(
                            f"""<Year>{i[0]}<Year>
                <Player>{i[1]}<Player>
                <Age>{i[2]}<Age>
                <Hometown>{i[3]}<Hometown>
                <State>{i[4]}<State>
                <Tm>{i[5]}<Tm>
                <G>{i[6]}<G>
                <GS>{i[7]}<GS>
                <Cmp>{i[8]}<Cmp>
                <Att>{i[9]}<Att>
                <Yds>{i[10]}<Yds>
                <TD>{i[11]}<TD>
                <Int>{i[12]}<Int>
                <Att>{i[13]}<Att>
                <Yds>{i[14]}<Yds>
                <Y/A>{i[15]}<Y/A>
                <TD>{i[16]}<TD>
                <Rec>{i[17]}<Rec>
                <Yds>{i[18]}<yDs>
                <Y/R>{i[19]}<Y/R>
                <TD>{i[20]}<TD>
                <FantPos>{i[21]}<FantPos>
                <FantPt>{i[22]}<FantPt>
                <Height (inches)>{i[23]}<Height (inches)>
                <Weight>{i[24]}<Weight>
                <College>{i[25]}<College>
                <Conference>{i[26]}<Conference>
                <College wins>{i[27]}<College wins>
                <College losses>{i[28]}<College losses>
                <DOB>{i[29]}<DOB>
                <Draft Round>{i[30]}<Draft Round>
                <Draft Year>{i[31]}<Draft Year>
                <Wonderlic>{i[32]}<Wonderlic>
                <40 Yard>{i[33]}<40 Yard>
                <Bench Press>{i[34]}<Bench Press>
                <Vert Leap(in)>{i[35]}<Vert Leap(in)>
                <Broad Jump(in)>{i[36]}<Broad Jump(in)>
                <Shuttle>{i[37]}<Shuttle>
                <3Cone>{i[38]}<3Cone>
            """)


main()