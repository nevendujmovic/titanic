# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 20:20:47 2021

@author: neven
"""

import pandas as pd

titanic_passengers = pd.read_csv('titanic_passengers_data_sample.csv')

query = titanic_passengers.head()

query01 = titanic_passengers.head(20)

query02 = titanic_passengers[['Name', 'Pclass', 'Survived']]

query03 = titanic_passengers[['PassengerId', 'Name', 'Age']]

query04 = titanic_passengers.drop_duplicates('Pclass')[['Pclass']]

query05 = titanic_passengers[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]\
                              .loc[titanic_passengers['Fare'] < 8]

query06 = titanic_passengers[['Name', 'Age', 'Pclass', 'Fare', 'Embarked']]\
          .loc[(titanic_passengers['Fare'] > 250) & \
             ((titanic_passengers['Embarked'] == 'S') | \
             (titanic_passengers['Embarked'] == 'C'))]


query07 = titanic_passengers[['Name', 'Age', 'Pclass', 'SibSp', 'Parch']]\
         .loc[titanic_passengers['Name'].str.contains('Fortune')]

query08 = titanic_passengers['Fare'].max()


query09 = titanic_passengers[['PassengerId']].\
    loc[(titanic_passengers['Survived'] == 'Yes')].count(axis = 0).\
        rename(index={'PassengerId': 'survived_passengers'})


query10 = titanic_passengers.groupby('Pclass')['Fare'].mean()\
    .reset_index()\
    .rename(columns={'Pclass': 'passenger_class', 'Fare': 'average_price'})


query11 = titanic_passengers[['Survived', 'Name', 'Age', 'Sex']]\
          .loc[(titanic_passengers['Survived'] == 'Yes')]\
          .sort_values(by=['Age'], ascending=False).head(10)

query12 = len(titanic_passengers) - titanic_passengers['Age'].count()

query12a = sum(pd.isnull(titanic_passengers['Age']))

print (titanic_passengers.isnull().sum(axis=0))

practice_query01 = titanic_passengers[['Embarked', 'PassengerId']]\
   .loc[(titanic_passengers['Embarked'] == 'C') | \
        (titanic_passengers['Embarked'] == 'S') | \
        (titanic_passengers['Embarked'] == 'Q')]
       
practice_query01 = practice_query01.groupby('Embarked')['PassengerId']\
                   .count()\
                   .reset_index(name='count')\
                   .sort_values(['count'], ascending=False)

practice_query02 = titanic_passengers[['Pclass', 'Sex', 'Age', 'PassengerId']]\
                   .groupby(['Pclass', 'Sex'])['Age']\
                   .mean()\
                   .reset_index(name='Average age')\
                   .sort_values(['Pclass'], ascending=True)

practice_query03 = titanic_passengers[['Name', 'Fare', 'Survived']]\
                   .sort_values(['Fare'], ascending=True)


practice_query04 = \
    titanic_passengers[['Pclass', 'Sex', 'Age', 'Survived', 'PassengerId']]\
   .loc[(titanic_passengers['Sex'] == 'male') & \
        (titanic_passengers['Survived'] == 'No') & \
            (titanic_passengers['Pclass'] == 3)]

practice_query04 = practice_query04[['Age', 'PassengerId']]['Age'].mean()


practice_query05 = \
    titanic_passengers[['Pclass', 'Sex', 'Age', 'Survived', 'PassengerId']]\
   .loc[(titanic_passengers['Sex'] == 'female') & \
        (titanic_passengers['Survived'] == 'Yes') & \
            (titanic_passengers['Pclass'] == 1)]

practice_query05 = practice_query05[['Age', 'PassengerId']]['Age'].mean()




