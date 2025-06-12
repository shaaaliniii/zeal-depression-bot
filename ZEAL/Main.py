import random
import json
import torch
import openai
from Brain import NeuralNet
from NeuralNetworks import bag_of_words, tokenize
from Tasks import NonInputExecution, InputExecution
from listen import Listen
from Speak import Say

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# OpenAI API setup
openai.api_key = "sk-...koVK"

# ------------------------------------------------

Name = "Zeal"

def Main():
    sentence = Listen()

    if sentence == "bye":
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        tag_found = False
        for intent in intents['intents']:
            if "tag" in intent:
                if tag == intent["tag"]:
                    tag_found = True
                    reply = random.choice(intent["responses"])
                    
                    if "time" in reply:
                        NonInputExecution(reply)
                    elif "date" in reply:
                        NonInputExecution(reply)
                    elif "wikipedia" in reply:
                        InputExecution(reply, sentence)
                    else:
                        Say(reply)
        
        if not tag_found:
            print("Tag not found in the intents JSON file.")

while True:
    Main()
    
    # Other imports and code above
