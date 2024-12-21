# Author Peter Golenev
# Purpose: Weight On Different Planets


# Input
sName= input("What is your name: ")

sWeight= input("What is your weight: ")
fWeight= float(sWeight)

print( sName, "here are your weights on our Solar System's planets:")


fMercury= fWeight*0.38
fVenus= fWeight*0.91
fOurMoon= fWeight*0.165
fMars= fWeight*0.38
fJupiter= fWeight*2.34
fSaturn= fWeight*0.93
fUranus= fWeight*0.92
fNeptune= fWeight*1.12
fPluto= fWeight*0.066

sMercury= print(format("Weight on Mercury:","25s"),format(fMercury,'10.2f'))

sVenus= print(format("Weight on Venus:","25s"),format(fVenus,'10.2f'))

sOurMoon= print(format("Weight on our Moon:",'25s'),format(fOurMoon,'10.2f'))

sMars= print(format("Weight on Mars:",'25s'),format(fMars,'10.2f'))

sJupiter= print(format("Weight on Jupiter:","25s"),format(fJupiter,'10.2f'))

sSaturn= print(format("Weight on Saturn:",'25s'),format(fSaturn,'10.2f'))

sUranus= print(format("Weight on Uranus:",'25s'),format(fUranus,'10.2f'))

sNeptune= print(format("Weight on Neptune:",'25s'),format(fNeptune,'10.2f'))

sPluto= print(format("Weight on Pluto:",'25s'),format(fPluto,'10.2f'))


