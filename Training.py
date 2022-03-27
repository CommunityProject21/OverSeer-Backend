# Importing libraries
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


df = pd.read_csv("Training.csv")
symptoms = list(df.columns)
df = df.drop(columns = "Unnamed: 133" , axis=1)

tp = df['prognosis'].unique()
lt = list(tp)
ql = ['Eat Yoghurt and Probiotics, Wash with Soap and Water  and Use Apple Cider Vinegar', ' Eat fruits which Rich in Vitamin C,Magnesium(like oranges,apples,almonds', 'Eat Ginger, Oatmeal and Vegetables: Vegetables are naturally low in fat and sugar., Non-citrus fruits, including melons, bananas, apples', 'whole fruits and vegetables,lean meaths,nuts,seeds and whole grains such as brown rice', 'Do not take vitamins at the same time you take other medicine,Do not mix medicine into hot drinks,Take all medicine with a full glass of water, unless your doctor tells you otherwise.', 'Apples, pears, oatmeal, and other foods that are high in fiber', 'Eating a diet high in vegetables, fruits, whole grains, and legumes, Include proteins, carbohydrates, and a little good fat in all meals and snacks', ' eat carbohydrates from fruit, vegetables, whole grains, beans, and low-fat or nonfat milk, as part of your diabetes meal plan', 'Low-fat cooked fish,Rice,Eggs,Pastas,Sugar-free cereals,Cooked vegetables', 'Eat plenty of fruits and vegetables. We still dont know which fruits and vegetables might have an effect on asthma, so the best advice is to increase your intake of a wide variety of them.', 'Low-salt, ready-to-eat cereals,Lean meat,Skinless turkey and chicken,Cooked hot cereal (not instant),Skim or 1% milk, yogurt, Greek yogurt (calcium-rich foods can lower blood pressure)', ' dark leafy greens, avocado, and tuna,Foods rich in omega-3 fatty acids include fish such as mackerel and salmon, and seeds and legumes.', 'Fish, nuts and oil seeds, Avoid red meat, white potato and coffee', 'Beans,Oatmeal,Tuna,Apples,Spinach',
      ' Look for high-fiber foods, such as oatmeal, berries, and almonds,Drink at least eight glasses of fluids per day,Eat at least 2 1/2 cups of veggies and 2 cups of fruit per day.', 'cereals, pulses, vegetables, fruits, milk and milk products, fish (stew), chicken (soup/stew), sugar, honey', 'mashed potatoes,sweet potatoes,avocado,scrambled eggs,beans and lentils,boiled chicken', 'Milk and dairy products,Beans, chickpeas, lentils, peas,eggs,Water, coconut water, natural fruit juices.', 'ripe bananas, melons, applesauce, canned fruit,potatoes, carrots, green beans, beets, squash', 'Plenty of fruits and vegetables,Whole grains such as oats, brown rice, barley, and quinoa,Healthy fats like those in nuts, avocados, and olive oil.', ' Plenty of fruits and vegetables,Whole grains such as oats, brown rice, barley, and quinoa,Healthy fats like those in nuts, avocados, and olive oil.', 'unsaturated fats, such as those in nuts and seeds, olive oil, and fish oils',
      'Plenty of fruits and vegetables.,Whole grains such as oats, brown rice, barley, and quinoa.,Low-fat or non-fat dairy products.', 'Olive oil, canola oil and flaxseed oil', ' a general diet containing 100 g/d of protein is appropriate. Provide supplemental multivitamins and minerals, including folate and thiamine', 'Fruits and vegetables like orange, mango, sweet pumpkin and carrots, guava, amla, tomato, nuts and seeds are an excellent source of Vitamin A, C and E.', 'Chicken soup,Broths,Coconut water,Hot tea,honey,ginger,spicy foods', 'diet rich in protein is beneficial for the people suffering from pneumonia. Foods like nuts, seeds, beans, white meat and cold water fishes like salmon and sardines have anti-inflammatory properties.', 'Whole grains,Broccoli and other cruciferous vegetables,Artichokes,Root vegetables', 'lots of fruits and vegetables,lean meats,fish,whole grains,nuts,beans,skinless poultry', 'Foods High in Rutin,Beets,Ginger,Asparagus,Watercress', 'vegetables, fruits, and lean meats. These are low in calories and very filling, which may help prevent weight gain.', 'Fresh or dried fruit. Fruits that provide the appropriate amount of carbohydrates include half a banana, 15 grapes, two tablespoons of raisins or a small apple or orange,Fruit juice,fat-free milk', 'Candy,Fresh or dried fruits,Fruit Juice,Fat-free milk,Hooney', 'Nuts,oily fish,Green tea,Garlic,Broccoli,Dark leafy greens', ' Fatty Fish. Salmon,Dark Leafy Greens. Spinach, kale, broccoli and collard greens,sources for vitamins E and C,nuts,green tea', 'Nuts,Strawberries and vitamin C sources food', 'yellow and orange fruits and vegetables such as carrots, apricots, and sweet potatoes,spinach and other dark green and leafy vegetables,tomatos,blueberries,brown rice', 'plain Greek yogurt, pickles, and sauerkraut,bananas, beans, lentils, nuts, oats', 'Fish, lean protein or plant-based proteins such as tofu or tempeh,Fruits and vegetables,Nuts and seeds,Small amounts of low-fat dairy', ' Garlic ,Ginger ,Chamomile ,Aloe vera for skin,Neem oil for skin , Honey']

encoder = LabelEncoder()
df["prognosis"] = encoder.fit_transform(df["prognosis"])

X = df.iloc[:,:-1]
Y = df.iloc[:, -1]
X_Train, X_Test, Y_Train, Y_Test =train_test_split(X, Y, test_size = 0.2, random_state = 2)

# Training and testing SVM Classifier
svm_model = SVC()
svm_model.fit(X_Train, Y_Train)

# Training and testing Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(X_Train, Y_Train)

# Training and testing Random Forest Classifier
rf_model = RandomForestClassifier(random_state=18)
rf_model.fit(X_Train, Y_Train)

# open a file where you want to store the data 
file  = open("svm_model.pkl", "wb")

# dump information to that file
pickle.dump(svm_model, file)

file.close()

file  = open("nb_model.pkl", "wb")
pickle.dump(nb_model, file)
file.close()

file  = open("rf_model.pkl", "wb")
pickle.dump(rf_model, file)
file.close()


symptoms = X.columns.values

# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
symptom_info=[]
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_info.append(symptom)
    symptom_index[symptom] = index

data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":encoder.classes_
}
