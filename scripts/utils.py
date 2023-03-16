import pandas as pd


class Setup:
    def __init__(self, data_files: list[str]) -> None:
        # will hold data
        data = pd.DataFrame()

        for path in data_files:
            # load data from file
            new_data = pd.read_csv(path)
            # combine with previous data
            data = pd.concat([data, new_data])

        # cleaning data
        cleaned_data = self.__clean_data(data)
        # saving data
        self.__data = cleaned_data

    def __rank_to_int(self, x):
        k = str(x)
        if 'P' in k:
            k = k[:-1]
        return int(k)

    def __clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        # making a copy
        df = data.copy()

        # removing duplicate values
        df.drop_duplicates(inplace=True)

        # converting rank to integer
        df['Opening Rank'] = df['Opening Rank'].apply(self.__rank_to_int)
        df['Closing Rank'] = df['Closing Rank'].apply(self.__rank_to_int)

        # removing faulty records
        data = data[~(data['Opening Rank'] > data['Closing Rank'])]

        # return clean data
        return df

    def get_branch_list(self, rank: int, seat_type: str, gender: str) -> list:
        # list of colleges
        colleges = []

        # required data
        required_data = pd.DataFrame()

        if gender == 'male':
            # only gender neutral seats
            required_data = self.__data[
                (self.__data['Seat Type'] == seat_type) &
                (self.__data['Gender'] == 'Gender-Neutral') &
                (self.__data['Opening Rank'] <= rank) &
                (self.__data['Closing Rank'] >= rank)
            ]
        elif gender == 'female':
            # all seats
            required_data = self.__data[
                (self.__data['Seat Type'] == seat_type) &
                (self.__data['Opening Rank'] <= rank) &
                (self.__data['Closing Rank'] >= rank)
            ]

        # adding to the list
        for i in range(len(required_data)):
            colleges.append({
                'institute': required_data.iloc[i]['Institute'],
                'program': required_data.iloc[i]['Academic Program Name']
            })

        return colleges
