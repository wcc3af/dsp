# Creating Dictionary with last name grouping

# create a new dataframe so we can manipulate the names
last_name_df = data.copy()

# Function to apply name splitting to get only the last name
def last_name(s):
    s_list = s.split(' ')
    return s_list[len(s_list)-1]

# apply the name splitting function to the data frame to make the name column last names only
last_name_df['name'] = last_name_df['name'].apply(last_name)

# Create the dictionary
last_name_dict = last_name_df.set_index('name').T.to_dict('list')


# With Full Name
full_name_dict = data.set_index('name').T.to_dict('list')

# sorted by last name
from collections import OrderedDict
sorted_full_name = OrderedDict(sorted(full_name_dict.items(),key=lambda x: x[0].split(' ')[len(x[0].split(' '))-1]))
