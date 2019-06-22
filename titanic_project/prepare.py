# Titanic Project - Kaggle
# Aquire File

from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder


def cabin_missing_data(i):
    '''
    Based on our research let's fill in the missing cabin info with the following:
    '''
    j = 0
    if i < 16:
        j = "G"
    elif i >= 16 and i < 27:
        j = "F"
    elif i >= 27 and i < 38:
        j = "T"
    elif i >= 38 and i < 47:
        j = "A"
    elif i >= 47 and i < 53:
        j = "E"
    elif i >= 53 and i < 54:
        j = "D"
    elif i >= 54 and i < 116:
        j = 'C'
    else:
        j = "B"
    return j


def handle_missing_values(df):
    '''
    Function that fills in missing values in each dataframe
    '''
    missing_value = df[(df.Pclass == 3) & (
        df.Embarked == "S") & (df.Sex == "male")].Fare.mean()

    return df.assign(
        Embarked=df.Embarked.fillna('C'),
        Cabin=df.Fare.apply(lambda x: cabin_missing_data(x)),
        Fare=df.Fare.fillna(missing_value)
    )


def encode_embarked(df):
    '''
    Function to encode the embarked column
    '''
    encoder = LabelEncoder()
    encoder.fit(df.Embarked)

    return df.assign(Embarked_Encode=encoder.transform(df.Embarked))


def prep_titanic_data(df):
    '''
    Function that prepares the dataframe using the functions above
    '''
    df = handle_missing_values(df)
    df = encode_embarked(df)

    return df
