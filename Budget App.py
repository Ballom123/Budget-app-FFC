

class Category:
    
    def __init__(self, name):
        
        self.title= name
        self.ledger= []

    def get_balance(self):
        
        sum=0
        for i in self.ledger:
            sum+=i["amount"] 
        return sum

    def deposit(self, amount: int, descrip=""):
        
        new_dict={"amount": amount, "description": descrip}
        self.ledger.append(new_dict)

    
    
    def withdraw(self, amount: int, descrip=""):
        #check if enough funds, just use get_balance
        
        curr_total= self.check_funds(amount)
        if curr_total is False:
            return False

        #actual withdraw
        elif curr_total is True:
            with_dic={"amount": -amount, "description": descrip}
            self.ledger.append(with_dic)
            return True



    def transfer(self, amount: int, otherCat):
        #transfer from category to other target category
        
        transferDescrip=f"Transfer to {otherCat.title}"
        if self.withdraw(amount, transferDescrip):
            receiveDescrip=f"Transfer from {self.title}"
            otherCat.deposit(amount, receiveDescrip)
            return True
        else: 
            return False    


    def check_funds(self, amount):
        
        sum=0
        for i in self.ledger:
            sum+=i["amount"] 
        if amount > sum:
            return False
        else:
            return True

    def __str__(self):
        #create title, subtract from 30, round, center, done BLAMMO fml
        
        nameLeng=len(self.title)
        firstHalf = int((30-nameLeng)/2)
        star = "*"
        nameLine = f"{star*firstHalf}{self.title}{star*firstHalf}"
        
        if len(nameLine) < 30:
            nameLine += star + "\n"
        else:
            nameLine += "\n"
        display = ""
        totalSum = 0
        
        #loop for ledger, a new line added to display
        
        for i in self.ledger:
            totalSum += i["amount"]
            newLine = ""
            start = i["description"]
            descLeng = len(start)
            if descLeng > 23:
                 newLine += start[:23]
            else:
                newLine += start
            number = "{:.2f}".format(i["amount"])
            leftAlign = 30-(len(newLine))-(len(number))
                
            newLine += " " * leftAlign + number + "\n"           
            display += newLine
        nameLine += display
        totalSum = "{:.2f}".format(totalSum)
        nameLine += f"Total: {totalSum}"

        return nameLine

def create_spend_chart(ledgers: list):
    
    #grab ledgers, calculate the withdrawls, make a total, make them into %s, round down to nearest 10s.
    withdrawls = []
    for i in ledgers:
        difference = 0
        for j in i.ledger:
            if j["amount"] < 0:
                difference += j["amount"]
        withdrawls.append(difference)
    #total of withdrawls
    totalDiff = sum(withdrawls)

    #create % values and round to nearest 10
    percentageList = []
    for i in withdrawls:
        percentage= round_down(((i/totalDiff)*100),)

        percentageList.append(percentage)

    #pair values with og ledger titles, prolly shouldve done from the start.
    chartDic = {}
    for i in range(len(ledgers)):
        name = ledgers[i].title
        value = percentageList[i]
        chartDic[name] = value


    chart = make_chart(chartDic)

    return chart

    

def make_chart(info: dict):
    #concatonates info from the formed dictionary into a printable chart
    
    x = 4
    
    #make dict into list Cat, amount
    catList = []
    catNumbers = []
    catAmount = 0
    for i, j in info.items():
        catList.append(i)
        catNumbers.append(j)
        catAmount += 1
    
    startLine = "Percentage spent by category\n"
    
    #make bargraphs, this could be optimized better, make +10 increment loop. fml
    
    line00 = "  0| "
    for number in catNumbers:
        if number >= 0:
            line00 += "o  "
    line00 += "\n"
    line10 = " 10| "
    for number in catNumbers:
        if number >= 10:
            line10 += "o  "
    line10 += "\n"
    line20 = " 20| "
    for number in catNumbers:
        if number >= 20:
            line20 += "o  "
    line20 += "\n"
    line30 = " 30| "
    for number in catNumbers:
        if number >= 30:
            line 30+= "o  "
    line30 += "\n"
    line40 = " 40| "
    for number in catNumbers:
        if number >= 40:
            line40 += "o  "
    line40 += "\n"
    line50 = " 50| "
    for number in catNumbers:
        if number >= 50:
            line50 += "o  "
    line50 += "\n"
    line60 = " 60| "
    for number in catNumbers:
        if number >= 60:
            line60 += "o  "
    line60 += "\n"
    line70 = " 70| "
    for number in catNumbers:
        if number >= 70:
            line70 += "o  "
    line70 += "\n"
    line80 = " 80| "
    for number in catNumbers:
        if number >= 80:
            line80 += "o  "
    line80 += "\n"
    line90 = " 90| "
    for number in catNumbers:
        if number >= 90:
            line90 += "o  "
    line90 += "\n"
    line100 = "100| "
    for number in catNumbers:
        if number >= 100:
            line100 += "o  "
    line100 += "\n"
    
    #collect lines into graph
    #bargraph X-axis line
    bottomLine = "    -" + ("---"*len(catList)) +"\n"
    startLine += line100+line90+line80+line70+line60+line50+line40+line30+line20+line10+line00+bottomLine

    #figure longest Cat title
    longestName = 0
    for i in catList:
        if len(i)>longestName:
            longestName = len(i)
    titlesLine = ""
    for i in range(longestName):
        newLine = "     "
        for word in catList:
            if (len(word)-1) >= i:
                newLine += f"{word[i]}  "
            else:
                newLine += "   "
        newLine += "\n"
        titlesLine += newLine


    startLine += titlesLine
    return startLine

def round_down(num):
    return num // 10 * 10


if __name__=="__main__":
    testixd = Category("Food")
    testixd.deposit(3000, "Savings")
    testixd.withdraw(32, "Veggies")
    testixd.withdraw(79, "Meat")
    testixd.deposit(300, "More MONEYMONEYMONEYMONEY")
    testi2 = Category("Clothes")
    testi2.deposit(200, "monthly allowance")
    testi2.withdraw(41, "pants")
    testixd.transfer(testi2, 10)

    
    print(create_spend_chart([testixd, testi2]))
