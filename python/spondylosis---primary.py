# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"N11z.00","system":"readv2"},{"code":"N11zz00","system":"readv2"},{"code":"N11..00","system":"readv2"},{"code":"17766.0","system":"readv2"},{"code":"20791.0","system":"readv2"},{"code":"41378.0","system":"readv2"},{"code":"56212.0","system":"readv2"},{"code":"53184.0","system":"readv2"},{"code":"54843.0","system":"readv2"},{"code":"55810.0","system":"readv2"},{"code":"65641.0","system":"readv2"},{"code":"23699.0","system":"readv2"},{"code":"51318.0","system":"readv2"},{"code":"96948.0","system":"readv2"},{"code":"96103.0","system":"readv2"},{"code":"829.0","system":"readv2"},{"code":"47024.0","system":"readv2"},{"code":"41516.0","system":"readv2"},{"code":"9834.0","system":"readv2"},{"code":"22452.0","system":"readv2"},{"code":"93977.0","system":"readv2"},{"code":"35851.0","system":"readv2"},{"code":"64854.0","system":"readv2"},{"code":"2001.0","system":"readv2"},{"code":"10121.0","system":"readv2"},{"code":"35838.0","system":"readv2"},{"code":"103137.0","system":"readv2"},{"code":"15015.0","system":"readv2"},{"code":"18205.0","system":"readv2"},{"code":"50448.0","system":"readv2"},{"code":"11688.0","system":"readv2"},{"code":"62914.0","system":"readv2"},{"code":"1565.0","system":"readv2"},{"code":"27583.0","system":"readv2"},{"code":"8920.0","system":"readv2"},{"code":"2881.0","system":"readv2"},{"code":"15744.0","system":"readv2"},{"code":"51531.0","system":"readv2"},{"code":"18826.0","system":"readv2"},{"code":"7429.0","system":"readv2"},{"code":"17092.0","system":"readv2"},{"code":"55628.0","system":"readv2"},{"code":"55238.0","system":"readv2"},{"code":"3447.0","system":"readv2"},{"code":"19386.0","system":"readv2"},{"code":"54852.0","system":"readv2"},{"code":"45730.0","system":"readv2"},{"code":"2294.0","system":"readv2"},{"code":"69912.0","system":"readv2"},{"code":"37097.0","system":"readv2"},{"code":"52991.0","system":"readv2"},{"code":"771.0","system":"readv2"},{"code":"38501.0","system":"readv2"},{"code":"18217.0","system":"readv2"},{"code":"1100.0","system":"readv2"},{"code":"56594.0","system":"readv2"},{"code":"48810.0","system":"readv2"},{"code":"5183.0","system":"readv2"},{"code":"63578.0","system":"readv2"},{"code":"58865.0","system":"readv2"},{"code":"71477.0","system":"readv2"},{"code":"8208.0","system":"readv2"},{"code":"63192.0","system":"readv2"},{"code":"M47.9","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('spondylosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["spondylosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["spondylosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["spondylosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
