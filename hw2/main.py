from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from data_loader import load_csv
from sklearn.impute import SimpleImputer
from simple_classifire import SimpleClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from visual import (
    add_histogram,
    add_lineplot,
    add_scatterplot,
    show_visualizations,
    add_survival_countplot,
    add_survival_heatmap,
    add_survival_by_sex
)



path = "dataset/titanic.csv"
df = load_csv(path)

label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])


df = df[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]



imputer = SimpleImputer(strategy='mean')
df[['Age', 'Fare']] = imputer.fit_transform(df[['Age', 'Fare']])


X = df.drop("Survived", axis=1)
y = df["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

classifier = SimpleClassifier(max_iter=200)
classifier.train(X_train, y_train)

accuracy = classifier.evaluate(X_test, y_test)
print(f"\nТочность модели: {accuracy:.2f}")


y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Матрица истинности:")
print(cm)


print("\nКлассификационный отчет:")
cr = classification_report(y_test, y_pred, target_names=["Not Survived", "Survived"])
print(cr)

add_histogram(df, "Age", save_path="visualizations/hist_age.png")
add_scatterplot(df, "Age", "Fare", save_path="visualizations/scatter_age_fare.png")
add_lineplot(df, "Pclass", "Fare", save_path="visualizations/line_pclass_fare.png")
add_survival_countplot(df, save_path="visualizations/survival_countplot.png")
add_survival_by_sex(df, save_path="visualizations/survival_by_sex.png")
add_survival_heatmap(df, save_path="visualizations/survival_heatmap.png")
show_visualizations()