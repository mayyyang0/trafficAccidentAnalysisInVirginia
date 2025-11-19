import pandas as pd

# 1. Read crash data for this specific street
df = pd.read_csv(r"D:\GIS\crash_BroadSt.csv")

# 2. Check column names and the first few rows
print(df.columns)
print(df.head())
print("Total number of crashes:", len(df))

# -------- 7.1 Roadway Conditions --------
print("\n=== ROADWAY_SU (Road Surface Condition) ===")
print(df['ROADWAY_SU'].value_counts(dropna=False))
print((df['ROADWAY_SU'].value_counts(normalize=True) * 100).round(1))

print("\n=== ROADWAY_AL (Road Alignment / Grade Type) ===")
print(df['ROADWAY_AL'].value_counts(dropna=False))
print((df['ROADWAY_AL'].value_counts(normalize=True) * 100).round(1))

if 'RD_CLASS' in df.columns:
    print("\n=== RD_CLASS (Road Classification) ===")
    print(df['RD_CLASS'].value_counts(dropna=False))
    print((df['RD_CLASS'].value_counts(normalize=True) * 100).round(1))

# -------- 7.2 Weather Conditions --------
print("\n=== WEATHER_CO (Weather Condition) ===")
print(df['WEATHER_CO'].value_counts(dropna=False))
print((df['WEATHER_CO'].value_counts(normalize=True) * 100).round(1))

# -------- 7.3 Lighting Conditions --------
print("\n=== LIGHT_COND (Lighting Condition) ===")
print(df['LIGHT_COND'].value_counts(dropna=False))
print((df['LIGHT_COND'].value_counts(normalize=True) * 100).round(1))

# -------- 7.4 Collision Type --------
print("\n=== COLLISION_ (Collision Type) ===")
print(df['COLLISION_'].value_counts(dropna=False))
print(df['COLLISION_'].value_counts(normalize=True).round(3))

# -------- 7.5 Pedestrian Involvement --------
print("\n=== PEDESTRIAN (Pedestrian Involvement) ===")
print(df['PEDESTRIAN'].value_counts(dropna=False))

# Calculate the percentage of pedestrian-involved crashes
# (Adjust the criteria depending on your coding scheme)
ped_flag = df['PEDESTRIAN'] > 0
ped_rate = ped_flag.mean() * 100
print(f"Percentage of crashes involving pedestrians: {ped_rate:.1f}%")

# -------- 7.6 Number of Vehicles --------
print("\n=== VEH_COUNT (Number of Vehicles Involved) ===")
print(df['VEH_COUNT'].value_counts().sort_index())
print(
    (df['VEH_COUNT'].value_counts(normalize=True) * 100)
    .sort_index()
    .round(1)
)

# -------- 7.7 Temporal Analysis: Year / Month / Hour --------
if 'CRASH_YEAR' in df.columns:
    print("\n=== Crash Count by Year ===")
    print(df['CRASH_YEAR'].value_counts().sort_index())

if 'CRASH_DATE' in df.columns:
    df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'])

    df['Month'] = df['CRASH_DATE'].dt.month
    df['Hour'] = df['CRASH_DATE'].dt.hour

    print("\n=== Crash Count by Month ===")
    print(df['Month'].value_counts().sort_index())

    print("\n=== Crash Count by Hour ===")
    print(df['Hour'].value_counts().sort_index())
