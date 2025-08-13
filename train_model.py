import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
def train_model():

    df = pd.read_csv("training_data.csv")
    X = df[["neg","neu","pos"]].values
    y = df["label"].values

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    clf = DecisionTreeClassifier(max_depth=3,random_state=42)
    clf.fit(X,y)
    print("Train accuracy: ", clf.score(x_train, y_train))
    print("Test accuracy: ", clf.score(x_test, y_test))
    # rules = export_text(clf, feature_names=["neg","neu","pos"])
    # print(rules)

