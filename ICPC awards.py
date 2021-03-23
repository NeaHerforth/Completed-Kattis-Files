#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''30
Seoul ACGTeam
VNU LINUX
SJTU Mjolnir
VNU WINDOWS
NTU PECaveros
HUST BKJuniors
HCMUS HCMUSSerendipity
VNU UBUNTU
SJTU Metis
HUST BKDeepMind
HUST BKTornado
HCMUS HCMUSLattis
NUS Tourism
VNU DOS
HCMUS HCMUSTheCows
VNU ANDROID
HCMUS HCMUSPacman
HCMUS HCMUSGeomecry
UIndonesia DioramaBintang
VNU SOLARIS
UIndonesia UIChan
FPT ACceptable
HUST BKIT
PTIT Miners
PSA PSA
DaNangUT BDTTNeverGiveUp
VNU UNIXBSD
CanTho CTUA2LTT
Soongsil Team10deung
Soongsil BezzerBeater'''

s=s.splitlines()
n=int(s[0])

uni_teams=[]
for i in range(1, len(s)):
    team=s[i].split()
    case=[]
    uni=team[0]
    team_name=team[1]
    case.append(uni)
    case.append(team_name)
    uni_teams.append(case)


#Find out who should get the first places
gold_uni=[]
gold_team=[]

i=0
while len(gold_uni)<4:
    if uni_teams[i][0] not in gold_uni:
        gold_uni.append(uni_teams[i][0])
        gold_team.append(uni_teams[i][1])
    i=i+1

#Find the second places
silver_uni=[]
silver_team=[]
i=i
while len(silver_uni)<4:
    if uni_teams[i][0] not in silver_uni and uni_teams[i][0] not in gold_uni :
        silver_uni.append(uni_teams[i][0])
        silver_team.append(uni_teams[i][1])
    i=i+1

#Find third places
bronze_uni=[]
bronze_team=[]
i=i
while len(bronze_uni)<4:
    if uni_teams[i][0] not in silver_uni and uni_teams[i][0] not in gold_uni and uni_teams[i][0] not in bronze_uni:
        bronze_uni.append(uni_teams[i][0])
        bronze_team.append(uni_teams[i][1])
    i=i+1

#Print everything correctly
for y in range(4):
    print(gold_uni[y], gold_team[y])
for x in range(4):
    print(silver_uni[x], silver_team[x])
for z in range(4):
    print(bronze_uni[z], bronze_team[z])
#Accepted