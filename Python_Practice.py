print("Hello World!")
#
counties=["Arapahoe","Denver","Jefferson"]
counties[0]
print(counties[2])
print(counties[-1])
#
len(counties)
#
counties[0:2]

counties.append("El Paso")
counties
#
counties.insert(2,"El Paso")
counties
#
counties.remove("El Paso")
counties
#
counties.pop(3)
counties
#
counties[0] ="El Paso"
counties
#
counties.insert(1,"Jefferson")
counties
#
counties[2]="Denver"
counties
#
counties[3]="Arapahoe"
counties
#
counties.remove("Arapahoe")
counties
#
counties.insert(0,"Arapahoe")
counties[1]="Denver"
counties[2]="Jefferson"
counties
#
counties_tuple=tuple()
counties_tuple=("Arapahoe","Denver","Jefferson")
len(counties_tuple)

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
counties_dict

len(counties_dict)

counties_dict.items()

counties_dict.keys()

counties_dict.values()

counties_dict.get("Denver")
#append

voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list pf counties.")
else:
    print("El Paso is not the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe"in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.") 

counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])

counties_tuple=("Araphahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
for county in counties_dict.keys():
    print(county)

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
for voters in counties_dict:
    print(counties_dict.get(county))

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
for key, value in counties_dict.items():
    print(key,value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)   

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# 3345 for candidate's votes and 23123 for the total votes

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

