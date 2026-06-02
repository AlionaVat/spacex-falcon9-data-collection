''
SpaceX Falcon 9 Data Collection using API
This script collects and prepares SpaceX Falcon 9 launch data using the SpaceX API.


# Requests allows us to make HTTP requests which we will use to get data from an API
import requests

# Pandas is used for data manipulation and analysis
import pandas as pd

# NumPy is used for numerical operations
import numpy as np

# Datetime is used to work with dates
import datetime


# Display all columns and full column values
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)


# Takes the dataset and uses the rocket column to call the API
# and append the data to the BoosterVersion list
def getBoosterVersion(data):
    for x in data["rocket"]:
        if x:
            response = requests.get(
                "https://api.spacexdata.com/v4/rockets/" + str(x)
            ).json()
            BoosterVersion.append(response["name"])


# Takes the dataset and uses the launchpad column to call the API
# and append longitude, latitude, and launch site name
def getLaunchSite(data):
    for x in data["launchpad"]:
        if x:
            response = requests.get(
                "https://api.spacexdata.com/v4/launchpads/" + str(x)
            ).json()
            Longitude.append(response["longitude"])
            Latitude.append(response["latitude"])
            LaunchSite.append(response["name"])


# Takes the dataset and uses the payloads column to call the API
# and append payload mass and orbit information
def getPayloadData(data):
    for load in data["payloads"]:
        if load:
            response = requests.get(
                "https://api.spacexdata.com/v4/payloads/" + load
            ).json()
            PayloadMass.append(response["mass_kg"])
            Orbit.append(response["orbit"])


# Takes the dataset and uses the cores column to call the API
# and append core-related data
def getCoreData(data):
    for core in data["cores"]:
        if core["core"] is not None:
            response = requests.get(
                "https://api.spacexdata.com/v4/cores/" + core["core"]
            ).json()
            Block.append(response["block"])
            ReusedCount.append(response["reuse_count"])
            Serial.append(response["serial"])
        else:
            Block.append(None)
            ReusedCount.append(None)
            Serial.append(None)

        Outcome.append(str(core["landing_success"]) + " " + str(core["landing_type"]))
        Flights.append(core["flight"])
        GridFins.append(core["gridfins"])
        Reused.append(core["reused"])
        Legs.append(core["legs"])
        LandingPad.append(core["landpad"])


# API endpoint for past SpaceX launches
spacex_url = "https://api.spacexdata.com/v4/launches/past"

response = requests.get(spacex_url)

print(response.content)


# Static dataset URL used in the original notebook
static_json_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json"
)

response = requests.get(static_json_url)

response.status_code


# Convert JSON response into a DataFrame
data = pd.json_normalize(response.json())

data.head()


# Select only the required columns
data = data[
    [
        "rocket",
        "payloads",
        "launchpad",
        "cores",
        "flight_number",
        "date_utc",
    ]
]


# Remove rows with multiple cores or multiple payloads
data = data[data["cores"].map(len) == 1]
data = data[data["payloads"].map(len) == 1]


# Extract single values from lists
data["cores"] = data["cores"].map(lambda x: x[0])
data["payloads"] = data["payloads"].map(lambda x: x[0])


# Convert date_utc to date format
data["date"] = pd.to_datetime(data["date_utc"]).dt.date


# Restrict launch dates
data = data[data["date"] <= datetime.date(2020, 11, 13)]


# Global variables
BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []


# Collect booster version data
getBoosterVersion(data)

BoosterVersion[0:5]


# Collect launch site data
getLaunchSite(data)


# Collect payload data
getPayloadData(data)


# Collect core data
getCoreData(data)


# Create launch dictionary
launch_dict = {
    "FlightNumber": list(data["flight_number"]),
    "Date": list(data["date"]),
    "BoosterVersion": BoosterVersion,
    "PayloadMass": PayloadMass,
    "Orbit": Orbit,
    "LaunchSite": LaunchSite,
    "Outcome": Outcome,
    "Flights": Flights,
    "GridFins": GridFins,
    "Reused": Reused,
    "Legs": Legs,
    "LandingPad": LandingPad,
    "Block": Block,
    "ReusedCount": ReusedCount,
    "Serial": Serial,
    "Longitude": Longitude,
    "Latitude": Latitude,
}


# Convert dictionary to DataFrame
df = pd.DataFrame(launch_dict)

df.head()


# Filter Falcon 9 launches
data_falcon9 = df[df["BoosterVersion"] != "Falcon 1"]

data_falcon9


# Reset FlightNumber column
data_falcon9.loc[:, "FlightNumber"] = list(range(1, data_falcon9.shape[0] + 1))

data_falcon9


# Check missing values
data_falcon9.isnull().sum()


# Calculate the mean value of PayloadMass
payload_mean = data_falcon9["PayloadMass"].mean()


# Check missing PayloadMass values
data_falcon9["PayloadMass"].isnull().sum()
