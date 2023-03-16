from scripts.utils import Setup


# list of data files
data_files = [
    "./data/round1_josaa_22.csv",
    "./data/round1_josaa_22.csv",
]

# setting up the system
setup = Setup(data_files)

# getting college list
college_list = setup.get_branch_list(
    rank=1000,
    seat_type='OPEN',
    gender='female'
)

# logging
print("No. of branch found:", len(college_list))
print("First two:", college_list[:2])
