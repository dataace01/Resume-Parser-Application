from ML_Pipeline import json_spacy
from ML_Pipeline import train_model
from ML_Pipeline import predict_model
from ML_Pipeline import text_extractor
from ML_Pipeline import utils


#####First lets create training data out of the tagged data############

train= json_spacy.convert_data_to_spacy(r"C:\Users\conta\OneDrive\Desktop\Project Pro\NLP Project to Build a Resume Parser in Python using Spacy\Resume_Parser_Code_Data\Resume_Parser_Code_Data\Resume_Parser\input\training\Entity Recognition in Resumes.json")

#print(train[0])
print("Done. Converted into spacy format")

print("Checking if previously built spacy model exists. If not, we will train a new one")

model=utils.check_existing_model("nlp_model")

model=train_model.build_spacy_model(train,model)

#test_text=text_extractor.convert_pdf_to_text(".\\Resume_Parser\\output\\")


predict_model.predict(r"C:\Users\conta\OneDrive\Desktop\Project Pro\NLP Project to Build a Resume Parser in Python using Spacy\Resume_Parser_Code_Data\Resume_Parser_Code_Data\Resume_Parser\output")


#mine = text_extractor.convert_pdf_to_text('.\\Resume_Parser\\input\\resumes\\resumes')

#print(test.head())

