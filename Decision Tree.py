import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# Simple dataset
data = {
    'Weather': ['Sunny','Sunny','Rainy','Rainy','Sunny'],
    'Windy': ['No','Yes','No','Yes','No'],
    'Play': ['Yes','No','Yes','No','Yes']
}

df = pd.DataFrame(data)

# Convert text to numbers
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

# Split input and output
X = df.drop('Play', axis=1)
y = df['Play']

# Train decision tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# Get tree rules
rules = tree.export_text(model, feature_names=['Weather','Windy'])

# Convert numeric output to readable structured format
rules = rules.replace("<= 0.50", "= No")
rules = rules.replace(">  0.50", "= Yes")
rules = rules.replace("class: 1", "Play = Yes")
rules = rules.replace("class: 0", "Play = No")

print("\nStructured Decision Tree:\n")
print(rules)
