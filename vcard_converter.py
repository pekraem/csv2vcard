import pandas as pd

df = pd.read_csv("~/Downloads/adressliste.csv",";",header=1)
df=df.replace("E-mail", "email")


#print df.Adresse.to_string().split()
#print df["E-Mail"]
#print df

cards = []
geb_d = []
geb_m = []
geb_y = []


for i in range(len(df)):
    #print df.Adresse[i].replace(","," ").split()
    if len(df.Adresse[i])<4:
        df.Adresse[i]="Str Nr Stadt plz"
    if df.Geburtstdatum[i]:
        geb_d.append((df.Geburtstdatum[i].split(".")[0]))
        geb_m.append((df.Geburtstdatum[i].split(".")[1]))
        geb_y.append((df.Geburtstdatum[i].split(".")[2]))
    vcard = '''
BEGIN:VCARD
VERSION:2.1
N:{Nachname};{vname};
FN:{vname} {Nachname}
TEL;TYPE=CELL,VOICE:{handy}
ADR;HOME:;;{street} {nr};{town};;{plz};{country}
EMAIL:{email}
BDAY:{geb}
END:VCARD
'''.format(Nachname=df.Nachname[i],
                vname=df.Vorname[i],
                handy=df.Handynummer[i],
                #street="s",
                #nr="1",
                #town="e",
                #plz="2",
                #email="JB",
                street=df.Adresse[i].replace(","," ").split()[0],
                nr=df.Adresse[i].replace(","," ").split()[1],
                town=df.Adresse[i].replace(","," ").split()[2],
                plz=df.Adresse[i].replace(","," ").split()[3],
                country="Deutschland",
                email=df["E-Mail"][i],
                geb=df.Geburtstdatum[i])
    cards.append(vcard)

df["vcard"] = cards
df["geb_d"] = geb_d
df["geb_m"] = geb_m
df["geb_y"] = geb_y

try:
    df["day"] = df["geb_d"].astype(int)
    df["year"] = df["geb_y"].astype(int)
except:
    df["day"] = df["geb_d"].astype(int)
df["month"] = df["geb_m"].astype(int)

#print df[["geb_d","geb_m","geb_y"]]
print df[df.month>=11].Vorname

string = ""
string = string.join(df["vcard"])
string.replace("    ","")

df.to_hdf('KJG_Adressen.h5', key='df', mode='w')

print string
with open("KJG_vcard.vcf","a") as vc:
    vc.write(string)

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
