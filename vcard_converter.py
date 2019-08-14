


class contact:
    """A class to store a contact in a dictionary and provide several functions to add, remove, change or export contacts"""
    vname   = ""
    nname   = ""
    adr     = ""
    geb     = 0
    handy   = 0
    email   = ""
    data    = None      #python dict with above data for better handling
    export  = True      #set export flag to false to avoid exporting as vcard
    exists  = False     #flag to check if contact already exists in database     ##### NOT IMPLEMENTED YET #####
    
    def __init__(self,dic):
     #   self.vname  = vN
    #    self.nname  = nN
   #     self.adr    = A
  #      self.geb    = G
 #       self.handy  = H
#        self.email  = E

        self.data   = dic
        self.vCard  = self.createVCard()

    def createVCard(self):
        vCard = '''
BEGIN:VCARD
VERSION:2.1
N:{nname};{vname};
FN:{vname} {nname}
TEL;TYPE=CELL,VOICE:{handy}
ADR;HOME:;;{street} {nr};{town};;{plz};{country}
EMAIL:{email}
BDAY:{geb}
END:VCARD
    '''.format(**self.data)
        return vCard

    def export(self,outfile):
        with open(outfile, "w") as ofile:
            ofile.write(self.vCard)


dummyDic = {
    "vname"     : "00xxx!",
    "nname"     : "yyy",
    "handy"     : "+99-000-66666",
    "street"    : "shitstreet",
    "nr"        : 88,
    "town"      : "shittycity",
    "plz"       : 12345,
    "country"   : "moon",
    "email"     : "b@st.ard",
    "geb"       : "1999-01-02"
    }

dummy = contact(dummyDic)
dummy.export("dummy.vcf")
