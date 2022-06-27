alph = {" ":"0","a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9",
        "j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17",
        "r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26"}

class encryptor:
    def __init__(self,shift=9): #contains all global values
        self.spaw = []
        self.shift = shift

    def actuallyEncrypt(self,lisT): #encrypts each letter
        numbers = []
        for letter in lisT:
            letter = str(int(letter) * self.shift)
            numbers.append(letter+".")
        return numbers
    def joiN(self,lisT): #joins list values into one string
        spaw = ''
        spaw = spaw.join(lisT)
        return spaw
    
    def encrypt(self,message=None): #main function run
        spaw = self.spaw
        for letter in message:
            letter = alph[letter]
            spaw.append(letter)

        spaw = self.actuallyEncrypt(spaw)
        spaw = self.joiN(spaw)
        return spaw


class decryptor:
    pass



def this():
    import this

