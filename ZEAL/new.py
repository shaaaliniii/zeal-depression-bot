import random
import json
import torch
from fuzzywuzzy import fuzz
from Brain import NeuralNet
from NeuralNetworks import bag_of_words, tokenize
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load patterns and intents from JSON file
with open(r'C:\Users\Shalini Singh\OneDrive\Desktop\ZEAL Depression Bot\ZEAL\intents.json', 'r') as file:
    data = json.load(file)
    intents = data['intents']
    
FILE = r"C:\Users\Shalini Singh\OneDrive\Desktop\ZEAL Depression Bot\ZEAL\TrainData.pth"
training_data = torch.load(FILE)

input_size = training_data["input_size"]
hidden_size = training_data["hidden_size"]
output_size = training_data["output_size"]
all_words = training_data["all_words"]
tags = training_data["tags"]
model_state = training_data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Zeal"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents:
            if "tag" in intent and tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                if tag == "goodbye":
                    return reply
                else:
                    return reply
                
    # If no exact match, check for fuzzy matches
    fuzzy_threshold = 80  # Adjust the threshold as needed
    for intent in intents:
        if "patterns" in intent:
            for pattern in intent["patterns"]:
                if fuzz.partial_ratio(msg, pattern) >= fuzzy_threshold:
                    reply = random.choice(intent["responses"])
                    return reply
            
    return "I do not understand.."
