import os
import json

DF_DIR = 'PaulHaleyAgent/intents'

def bio_format(training_phrases_filename):
    with open(os.path.join(DF_DIR, training_phrases_filename)) as file:
        intent_name = training_phrases_filename.split("_usersays")[0]
        training_phrases = json.load(file)

    for phrase in training_phrases:
        raw, bio = [], []
        for span in phrase['data']:
            if span['text'] == ' ':
                pass
            elif 'alias' in span.keys():
                listed = span['text'].split(' ')
                bio.append("B-"+span['alias'])
                if len(listed) > 1:
                    for z in listed[1:]:
                        bio.append("I-"+span['alias'])
            else:
                listed = (span['text'].strip()).split(' ')
                bio.append((len(listed)*'O ').strip())
            raw.append(span['text'])
        with open(os.path.join('label.txt'), "a") as f:
            f.write(intent_name+'\n')
        with open(os.path.join('seq.in'), "a") as f:
            f.write(''.join(raw)+'\n')
        with open(os.path.join('seq.out'), "a") as f:
            f.write(' '.join(bio)+'\n')
        
if __name__ == "__main__":
    for filename in os.listdir(os.path.join(DF_DIR)):
        if 'usersays' in filename:
            bio_format(filename)
        