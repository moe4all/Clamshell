import os
import os.path
import json
import re


class EmptyClass:
    pass

def EmptyMethod():
    pass

@staticmethod
def EmptyStaticMethod():
    pass
    
def VariablesInInstance(Instance):
    EmptyClassInstanceDictionaryKeys=list(dict(EmptyClass.__dict__).keys())
    InstanceDictionary=dict(type(Instance).__dict__)
    InstanceDictionaryKeys=list(InstanceDictionary.keys())
    Cursor=0
    End=InstanceDictionaryKeys.__len__()
    while(Cursor<End):
        InstanceDictionaryKey=InstanceDictionaryKeys[Cursor]
        if((InstanceDictionaryKey in EmptyClassInstanceDictionaryKeys)or
           (type(InstanceDictionary[InstanceDictionaryKey])==type(EmptyMethod))or
           (type(InstanceDictionary[InstanceDictionaryKey])==type(EmptyStaticMethod))):
            del(InstanceDictionary[InstanceDictionaryKey])
        Cursor=Cursor+1
    return InstanceDictionary

class Daton():
    def ToDictionary(self):
        Variables=VariablesInInstance(self)
        Contents=self.__dict__
        ContentKeys=Contents.keys()
        for ContentKey in ContentKeys:
            if(ContentKey in Variables.keys()):
                Variables[ContentKey]=Contents[ContentKey]
        return Variables
    def ToList(self,Header=None):
        Dictionary=self.ToDictionary()
        DesiredHeader=Header
        if(DesiredHeader==None):
            DesiredHeader=Dictionary.keys()
        List=[]
        for HeaderUnit in DesiredHeader:
            List.append(Dictionary[HeaderUnit])
        return List

class LanguageCodeAdapter():
    '''
    The class that transforms international standardized language code to name of language, or vise-versa
    '''
    Afrikaans={"Code":"afr","Name":"Afrikaans"}
    Arabic={"Code":"ara","Name":"Arabic"}
    Basque={"Code":"eus","Name":"Basque"}
    Cantonese={"Code":"zho-yue","Name":"Cantonese"}
    Catalan={"Code":"cat","Name":"Catalan"}
    Chinese={"Code":"zho","Name":"Chinese"}
    Cree={"Code":"crl","Name":"Cree"}
    Croatian={"Code":"hrv","Name":"Croatian"}
    Czech={"Code":"ces","Name":"Czech"}
    Danish={"Code":"dan","Name":"Danish"}
    Dutch={"Code":"nld","Name":"Dutch"}
    English={"Code":"eng","Name":"English"}
    Estonian={"Code":"est","Name":"Estonian"}
    Farsi={"Code":"fas","Name":"Farsi"}
    Finnish={"Code":"sun","Name":"Finnish"}
    French={"Code":"fra","Name":"French"}
    Galician={"Code":"glg","Name":"Galician"}
    German={"Code":"deu","Name":"German"}
    Greek={"Code":"ell","Name":"Greek"}
    Hebrew={"Code":"heb","Name":"Hebrew"}
    Hungarian={"Code":"hun","Name":"Hungarian"}
    Icelandic={"Code":"isl","Name":"Icelandic"}
    Indonesian={"Code":"ind","Name":"Indonesian"}
    Irish={"Code":"gle","Name":"Irish"}
    Italian={"Code":"ita","Name":"Italian"}
    Japanese={"Code":"jpn","Name":"Japanese"}
    Javanese={"Code":"jav","Name":"Javanese"}
    Kannada={"Code":"kan","Name":"Kannada"}
    Kikuyu={"Code":"kik","Name":"Kikuyu"}
    Korean={"Code":"kor","Name":"Korean"}
    Lithuanian={"Code":"lit","Name":"Lithuanian"}
    Norwegian={"Code":"nor","Name":"Norwegian"}
    Polish={"Code":"pol","Name":"Polish"}
    Portuguese={"Code":"por","Name":"Portuguese"}
    Punjabi={"Code":"pan","Name":"Punjabi"}
    Romanian={"Code":"ron","Name":"Romanian"}
    Russian={"Code":"rus","Name":"Russian"}
    Sesotho={"Code":"sot","Name":"Sesotho"}
    Spanish={"Code":"spa","Name":"Spanish"}
    Swahili={"Code":"swa","Name":"Swahili"}
    Swedish={"Code":"swe","Name":"Swedish"}
    Tagalog={"Code":"tag","Name":"Tagalog"}
    Taiwanese={"Code":"zho-min","Name":"Taiwanese"}
    Tamil={"Code":"tam","Name":"Tamil"}
    Thai={"Code":"tha","Name":"Thai"}
    Turkish={"Code":"tur","Name":"Turkish"}
    Vietnamese={"Code":"vie","Name":"Vietnamese"}
    Welsh={"Code":"cym","Name":"Welsh"}
    Yiddish={"Code":"yid","Name":"Yiddish"}
    
    @staticmethod
    def ValidLanguages():
        '''
        List all available languages
        Output:
            A list of language dictionary, within which are language codes and language names
        '''
        Instance=LanguageCodeAdapter()
        Languages=VariablesInInstance(Instance)
        return Languages

    @staticmethod
    def ValidCodes():
        '''
        List all available language codes
        Output: 
            A list of language codes
        '''
        Languages=LanguageCodeAdapter.ValidLanguages()
        Codes=[]
        for Language in Languages:
            Code=Language["Code"]
            Codes.append(Code)
        return Codes
    
    @staticmethod
    def ValidNames():
        '''
        List all available language names
        Output:
            A list of language names
        '''
        Languages=LanguageCodeAdapter.ValidLanguages()
        Names=[]
        for Language in Languages:
            Name=Language["Name"]
            Names.append(Name)
        return Names
    
    @staticmethod
    def Code2Name(Code):
        '''
        Transform language code to language name
        Input:
            Code: a language code
        Output:
            The corresponding language name
        '''
        Languages=LanguageCodeAdapter.ValidLanguages()
        for Language in Languages:
            if(Language["Code"]==Code):
                return Language
        return None

    @staticmethod
    def Name2Code(Name):
        '''
        Transform language name to language code
        Input:
            Name: a language name
        Output:
            The corresponding language code
        '''
        Languages=LanguageCodeAdapter.ValidLanguages()
        for Language in Languages:
            if(Language["Name"]==Name):
                return Language
        return None

class Sketch(Daton):
    '''
    The basic class storing result of initial processing on framework
    '''
    Type=None
    Tag=None
    Content=None
    Dependents=None
    
    def __init__(self,Type=None,Tag=None,Content=None,Dependents=[]):
        '''
        Creating a new instance of Sketch
        Input:
            Type: the type of sketch, can be Header, Main or Dependent
            Tag: the initial part of data before colon(:), for example "Jim" in "Jim:Hello"
            Content: the rest part of data after colon(:), for example "Hello" in "Jim:Hello"
            Dependents: a list of sketches, representing the depending tiers
        Output:
            A new instance of Sketch
        '''
        self.Type=Type
        self.Tag=Tag
        self.Content=Content
        self.Dependents=Dependents

    @staticmethod
    def SketchTypeHeader():
        return "Header"
    
    @staticmethod
    def SketchTypeMain():
        return "Main"
    
    @staticmethod
    def SketchTypeDependent():
        return "Dependent"

class Participant(Daton):
    Code=None
    Name=None
    StandardRole=None
    Language=None
    Corpus=None
    Age=None
    Sex=None
    Group=None
    SES=None
    IDRole=None
    Education=None
    Custom=None

    @staticmethod
    def StandardIDLabels():
        return ["Language","Corpus","Code","Age","Sex","Group","SES","IDRole","Education","Custom"]
    
    @staticmethod
    def StandardParticipantLabels():
        return ["Code","Name","StandardRole"]

    def __init__(self,Code=None,Name=None,StandardRole=None,
    Language=None,Corpus=None,Age=None,Sex=None,Group=None,SES=None,IDRole=None,Education=None,Custom=None):
        self.Code=Code
        self.Name=Name
        self.StandardRole=StandardRole
        self.Language=Language
        self.Corpus=Corpus
        self.Age=Age
        self.Sex=Sex
        self.Group=Group
        self.SES=SES
        self.IDRole=IDRole
        self.Education=Education
        self.Custom=Custom
    
    def ImportParticipantPart(self,ParticipantPart):
        Cells=ParticipantPart.split(" ")
        if(Cells.__len__()>=3):
            self.Code=Cells[0]
            self.Name=Cells[1]
            self.StandardRole=Cells[2]
        elif(Cells.__len__()==2):
            self.Code=Cells[0]
            self.StandardRole=Cells[1]
        elif(Cells.__len__()==1):
            self.Code=Cells[0]
    
    def ImportIDSketch(self,IDSketch):
        IDContent=IDSketch.Content
        Cells=IDContent.split("|")
        Code=Cells[2]
        if(not((self.Code==None)or(self.Code==Code))):
            return
        self.Language=Cells[0]
        self.Corpus=Cells[1]
        self.Code=Cells[2]
        self.Age=Cells[3]
        self.Sex=Cells[4]
        self.Group=Cells[5]
        self.SES=Cells[6]
        self.IDRole=Cells[7]
        self.Education=Cells[8]
        self.Custom=Cells[9]
    
class Main(Daton):
    SpeakerCode=None
    Sketch=None
    Words=None
    Parameters=None
    Dependents=None
    
    def __init__(self,SpeakerCode=None,Sketch=None,Words=[],Parameters=[],Dependents=[]):
        self.SpeakerCode=SpeakerCode
        self.Sketch=Sketch
        self.Words=Words
        self.Parameters=Parameters
        self.Dependents=Dependents
    
    @staticmethod
    def DeleteConsecutiveSpace(Content):
        '''
        '''
        Buffer=Content
        while(Buffer.find("  ")>=0):
            Buffer=Buffer.replace("  "," ")
        return Buffer

    def HandleSpecialMarker(self,Content):
        '''
        '''
        Segments=Content.split(" ")
        Handled=""
        for Segment in Segments:
            Index=Segment.find("@")
            if(Index>=0):
                Parts=Segment.split("@")
                Scope=Parts[0]
                Note="@"+Parts[1]
                ThisParameter=Parameter(Scope=Scope,Note=Note)
                self.Parameters.append(ThisParameter)
                Handled=Handled+Segment.replace(Note,"")+" "
            else:
                Handled=Handled+Segment+" "

        Handled=Handled[:-1]
        Handled=Main.DeleteConsecutiveSpace(Handled)
        return Handled
    
    def HandleSimpleEvent(self,Content):
        Segments=Content.split(" ")
        Handled=""
        for Segment in Segments:
            Index=Segment.find("&=")
            if(Index>=0):
                Parts=Segment.split("&=")
                Scope=Content
                Note="&="+Parts[1]
                ThisParameter=Parameter(Scope=Scope,Note=Note)
                self.Parameters.append(ThisParameter)
                Handled=Handled+Segment.replace(Note,"")+" "
            else:
                Handled=Handled+Segment+" "
        Handled=Handled[:-1]
        Handled=Main.DeleteConsecutiveSpace(Handled)
        return Handled
    
    def HandleInterposedWord(self,Content):
        Segments=Content.split(" ")
        Handled=""
        for Segment in Segments:
            Index=Segment.find("&*")
            if(Index>=0):
                Parts=Segment.split("&*")
                Scope=Content
                Note="&*"+Parts[1]
                ThisParameter=Parameter(Scope=Scope,Note=Note)
                self.Parameters.append(ThisParameter)
                Handled=Handled+Segment.replace(Note,"")+" "
            else:
                Handled=Handled+Segment+" "
        Handled=Handled[:-1]
        Handled=Main.DeleteConsecutiveSpace(Handled)
        return Handled
    
    def HandlePause(self,Content):
        Segments=Content.split(" ")
        Handled=""
        for Segment in Segments:
            Index1=Segment.find("(.)")
            Index2=Segment.find("(..)")
            Index3=Segment.find("(...)")
            if((Index1>=0)or
            (Index2>=0)or
            (Index3>=0)):
                Scope=Content
                if(Index1>=0):
                    Note="(.)"
                elif(Index2>=0):
                    Note="(..)"
                elif(Index3>=0):
                    Note="(...)"
                ThisParameter=Parameter(Scope=Scope,Note=Note)
                self.Parameters.append(ThisParameter)
                Handled=Handled+Segment.replace(Note,"")+" "
            else:
                Handled=Handled+Segment+" "
        Handled=Handled[:-1]
        Handled=Main.DeleteConsecutiveSpace(Handled)
        return Handled
    def HandleLongVocalEvent(self,Content):
        Handled=Content
        return Handled
    def HandleLongNonvocalEvent(self,Content):
        Handled=Content
        return Handled
    
    def HandleScopedSymbol(self,Content):
        Rest=Content
        Pattern="\\<(.*?)\\> \\[(.*?)\\](.*)"
        Handled=Content
        while(Rest.__len__()>0):
            Matched=re.search(Pattern,Rest)
            if((not(Matched==None))and(Matched.lastindex>=3)):
                Scope=Matched.group(1)
                Note="["+Matched.group(2)+"]"
                ThisParameter=Parameter(Scope=Scope,Note=Note)
                self.Parameters.append(ThisParameter)
                Handled=Handled.replace("<"+Scope+">",Scope)
                Handled=Handled.replace(Note,"")
                Rest=Matched.group(3)
            else:
                break
        Handled=Main.DeleteConsecutiveSpace(Handled)
        return Handled
    
    def HandleSquareBraketedSymbol(self,Content):
        Rest=Content
        Pattern="\\[(.*?)\\](.*)"
        Handled=Content
        while(Rest.__len__()>0):
            Matched=re.search(Pattern,Rest)
            if((not(Matched==None))and(Matched.lastindex>=2)):
                Scope=Content
                Note="["+Matched.group(1)+"]"
                ThisParameter=Parameter(Scope=Scope,Note=Note)
                self.Parameters.append(ThisParameter)
                Handled=Handled.replace(Note,"")
                Rest=Matched.group(2)
            else:
                break
        Handled=Main.DeleteConsecutiveSpace(Handled)
        return Handled
    
    def HandleEvents(self,Content):
        '''
        '''
        Handled=Content
        Handled=self.HandleScopedSymbol(Handled)
        Handled=self.HandleSquareBraketedSymbol(Handled)
        Handled=self.HandleLongVocalEvent(Handled)
        Handled=self.HandleLongNonvocalEvent(Handled)
        Handled=self.HandlePause(Handled)
        Handled=self.HandleSimpleEvent(Handled)
        Handled=self.HandleSpecialMarker(Handled)
        return Handled
        
    def ImportMainSketch(self,MainSketch):
        '''
        '''
        self.SpeakerCode=MainSketch.Tag
        self.Sketch=MainSketch
        Handled=self.Sketch.Content
        Handled=self.HandleEvents(Handled)
        Cells=Handled.split(" ")
        for Cell in Cells:
            ThisWord=Word(Plain=Cell)
            self.Words.append(ThisWord)
        Dependets=MainSketch.Dependents
        for Dependent in Dependets:
            if(Dependent.Tag=="mor"):
                ThisMor=Mor()
                ThisMor.ImportMorSegment(Dependent.Content)
                self.Dependents.append(ThisMor)
            else:
                self.Dependents.append(Dependent)
        
class Mor(Daton):
    '''
    '''
    Plain=None
    Morphemes=None
    Parameters=None
    def __init__(self,Plain=None,Morphemes=[],Parameters=[]):
        self.Plain=Plain
        self.Morphemes=Morphemes
        self.Parameters=Parameters
    def ImportMorSegment(self,MorSegment):
        '''
        '''
        Cells=MorSegment.split("~")
        if(Cells.__len__()==1):
            ThisMorpheme=Morpheme()
            ThisMorpheme.ImportMorPart(Cells[0])
            self.Morphemes.append(ThisMorpheme)
        elif(Cells.__len__()>1):
            CellCursor=0
            while(CellCursor<Cells.__len__()):
                ThisMorPart=Cells[CellCursor]
                ThisMorpheme=Morpheme()
                ThisMorpheme.ImportMorPart(ThisMorPart)
                self.Morphemes.append(ThisMorpheme)
                CellCursor=CellCursor+1 

class Morpheme(Daton):
    '''
    '''
    Content=None
    Category=None
    Parameters=None
    def __init__(self,Content=None,Category=None,Parameters=[]):
        self.Content=Content
        self.Category=Category
        self.Parameters=Parameters
    def ImportMorPart(self,MorPart):
        Cells=MorPart.split("|")
        if(Cells.__len__()>=2):
            self.Content=Cells[1]
            self.Category=Cells[0]
        elif(Cells.__len__()==1):
            self.Content=Cells[0]

class Word(Daton):
    '''
    '''
    Plain=None
    Parameters=None
    def __init__(self,Plain=None,Parameters=[]):
        '''
        '''
        self.Plain=Plain
        self.Parameters=Parameters

class Parameter(Daton):
    '''
    '''
    Scope=None
    Note=None
    def __init__(self,Scope=None,Note=None):
        '''
        '''
        self.Scope=Scope
        self.Note=Note 

class Clamshell(Daton):
    '''
    '''
    ChaHomePath=None
    ChaPaths=None
    Sketches=None
    Participants=None
    Mains=None

    def __init__(self,ChaHomePath=None,ChaPaths=[],Sketches=[],Participants=[],Mains=[]):
        '''
        '''
        self.ChaHomePath=ChaHomePath
        self.ChaPaths=ChaPaths
        self.Sketches=Sketches
        self.Participants=Participants
        self.Mains=Mains

    @staticmethod
    def ReadClamshellFile(ClamshellPath):
        '''
        '''
        File=open(ClamshellPath,"r",-1,"utf-8")
        Content=File.read()
        Clamshell=json.loads(Content)
        File.close()
        return Clamshell

    @staticmethod
    def WriteClamshellFile(Clamshell,ClamshellPath):
        '''
        '''
        File=open(ClamshellPath,"w",-1,"utf-8")
        Content=json.dumps(Clamshell)
        Content=File.write(Content)
        File.flush()
        File.close()
    
    @staticmethod
    def ListChaPathInFolder(FolderPath):
        '''
        '''
        FuturePaths=[FolderPath]
        ChaPaths=[]
        while(FuturePaths.__len__()>0):
            PresentPaths=FuturePaths
            FuturePaths=[]
            for PresentPath in PresentPaths:
                Names=os.listdir(PresentPath)
                for Name in Names:
                    Path=PresentPath+Name
                    if(os.path.isdir(Path)):
                        FuturePath=Path+"/"
                        FuturePaths.append(FuturePath)
                    if(os.path.isfile(Path)):
                        if(Path[-4:]==".cha"):
                            ChaPaths.append(Path)
        return ChaPaths

    @staticmethod
    def ReadChaFile(ChaPath):
        '''
        '''
        File=open(ChaPath,"r",-1,"utf-8")
        Content=File.read()
        File.close()
        return Content

    @staticmethod
    def SplitChaLines(ChaContent):
        '''
        '''
        Lines=ChaContent.split("\n")
        ChaLines=[]
        Cursor=-1
        ChaLine=""
        while(Cursor<Lines.__len__()):
            Cursor=Cursor+1
            Line=Lines[Cursor]
            if(ChaLine==""):
                ChaLine=ChaLine+Line
                continue
            if((Line[0]=="@")or
                (Line[0]=="*")or
                (Line[0]=="%")
                ):
                ChaLines.append(ChaLine)
                ChaLine=Line
                if(Line=="@End"):
                    ChaLines.append(ChaLine)
                    break
                continue
            if(Line[0]=="\t"):
                ChaLine=ChaLine+" "+Line[1:]
        return ChaLines
    
    @staticmethod
    def MakeSketchesFromChaLines(ChaLines):
        '''
        '''
        Sketches=[]
        ChaLineCursor=0
        SketchCursor=-1
        while(ChaLineCursor<ChaLines.__len__()):
            ChaLine=ChaLines[ChaLineCursor]
            Tag=None
            Content=None
            Index=ChaLine.find(":\t")
            if(Index>=0):
                Tag=ChaLine[1:Index]
                Content=ChaLine[Index+2:]
            else:
                Tag=ChaLine[1:]
                Content=""
            if(ChaLine[0]=="@"):
                ThisSketch=Sketch(
                    Type=Sketch.SketchTypeHeader(),
                    Tag=Tag,
                    Content=Content,
                    Dependents=[]
                )
                Sketches.append(ThisSketch)
                SketchCursor=SketchCursor+1
            if(ChaLine[0]=="*"):
                ThisSketch=Sketch(
                    Type=Sketch.SketchTypeMain(),
                    Tag=Tag,
                    Content=Content,
                    Dependents=[]
                )
                Sketches.append(ThisSketch)
                SketchCursor=SketchCursor+1
            if(ChaLine[0]=="%"):
                ThisSketch=Sketch(
                    Type=Sketch.SketchTypeDependent,
                    Tag=Tag,
                    Content=Content,
                    Dependents=[]
                )
                Sketches[SketchCursor].Dependents.append(ThisSketch)
            ChaLineCursor=ChaLineCursor+1
        return Sketches
    
    def MakeSketches(self):
        '''
        '''
        FolderPath=self.ChaHomePath
        ChaPaths=Clamshell.ListChaPathInFolder(FolderPath)
        self.ChaPaths=ChaPaths
        for ChaPath in ChaPaths:
            ChaContent=Clamshell.ReadChaFile(ChaPath)
            ChaLines=Clamshell.SplitChaLines(ChaContent)
            TheseSketches=Clamshell.MakeSketchesFromChaLines(ChaLines)
            self.Sketches=self.Sketches+TheseSketches
    
    def ParseParticipants(self):
        '''
        '''
        for ThisSketch in self.Sketches:
            if(ThisSketch.Type==Sketch.SketchTypeHeader()):
                if(ThisSketch.Tag=="Participants"):
                    ParticipantContent=ThisSketch.Content
                    ParticipantParts=ParticipantContent.split(",")
                    for ParticipantPart in ParticipantParts:
                        ThisParticipant=Participant()
                        ThisParticipant.ImportParticipantPart(ParticipantPart)
                        self.Participants.append(Participant)
                if(ThisSketch.Tag=="ID"):
                    BufferParticipant=Participant()
                    BufferParticipant.ImportIDSketch(ThisSketch)
                    ParticipantCursor=0
                    while(ParticipantCursor<self.Participants.__len__()):
                        if(self.Participants[ParticipantCursor].Code==BufferParticipant.Code):
                            self.Participants[ParticipantCursor].ImportIDSketch(ThisSketch)
                            break
                        ParticipantCursor=ParticipantCursor+1

    def ParseMains(self):
        '''
        '''
        for ThisSketch in self.Sketches:
            if(ThisSketch.Type==Sketch.SketchTypeMain()):
                ThisMain=Main(SpeakerCode=None,Sketch=None,Words=[],Parameters=[],Dependents=[])
                print(ThisMain.ToDictionary()["Parameters"].__len__())
                ThisMain.ImportMainSketch(ThisSketch)
                self.Mains.append(ThisMain)

    def ParseSketches(self):
        '''
        '''
        self.ParseParticipants()
        self.ParseMains()

    
    def Parse(self):
        '''
        '''
        self.MakeSketches()
        self.ParseSketches()

        
