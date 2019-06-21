from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder


def cabin_missing_data(i):

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

    missing_value = df[(df.Pclass == 3) & (df.Embarked == "S")
                       & (df.Sex == "male")].Fare.mean()

    return df.assign(
        Embarked=df.Embarked.fillna('C', inplace=True),
        Cabin=df.Fare.apply(lambda x: cabin_missing_data(x)),
        Fare=df.Fare.fillna(missing_value, inplace=True)
    )


def encode_embarked(df):

    encoder = LabelEncoder()
    encoder.fit(df.embarked)

    return df.assign(embarked_encode=encoder.transform(df.embarked))


def prep_titanic_data(df):

    df = df.pipe(handle_missing_values)\
        .pipe(encode_embarked)

    return df
