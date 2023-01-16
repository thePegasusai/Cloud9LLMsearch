import torch
from torchtext import data
import re

# Define your text field
text_field = data.Field(tokenize='spacy')

# Load your dataset
train_data, test_data = data.TabularDataset.splits(path='path/to/data', train='train.csv', test='test.csv', format='csv', fields=[('text', text_field), ('label', label_field)])

# Build the vocabulary
text_field.build_vocab(train_data, min_freq=2)

# Define a function to convert text to integer
def text_to_int(text):
    return text_field.process([text])[0].v

# Define a function to convert integer to text
def int_to_text(int_list):
    return text_field.vocab.itos[int_list]

class LSTM(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, bidirectional, dropout):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.lstm = torch.nn.LSTM(embedding_dim, hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout)
        self.fc = torch.nn.Linear(hidden_dim * 2, output_dim)
        self.dropout = torch.nn.Dropout(dropout)
        
    def forward(self, text, text_lengths):
        #text = [sent len, batch size]
        embedded = self.dropout(self.embedding(text))
        #embedded = [sent len, batch size, emb dim]
        #pack sequence
        packed_embedded = torch.nn.utils.rnn.pack_padded_sequence(embedded, text_lengths)
        packed_output, (hidden, cell) = self.lstm(packed_embedded)
        #unpack sequence
        output, output_lengths = torch.nn.utils.rnn.pad_packed_sequence(packed_output)
        #output = [sent len, batch size, hid dim * num directions]
        #output over padding tokens are zero tensors
        
        #concat the final forward and backward hidden state
        hidden = self.dropout(torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim = 1))
                
        #hidden = [batch size, hid dim * num directions]
        return self.fc(hidden)
        
def create_prompt(emoji_dict):
    prompt = input("Enter your message: ")
    # Parse emojis
    for emoji, code in emoji_dict.items():
        prompt = re.sub(emoji, code, prompt)
    return prompt

emoji_dict = {':)': '😊', ':(': '😔'}
prompt = create_prompt(emoji_dict)
# convert prompt to integers using the text_to_int function
prompt_int = text_to_int(prompt)

# pass prompt_int to the LSTM model

output = model(prompt_int)

# convert output back to text using the int_to_text function

output_text = int_to_text(output)

print(output_text)

# 
In this example, all of the code snippets are combined into one file, and they are called in sequence. The user is prompted to enter a message, the emojis in the message are parsed, the message is tokenized and converted to integers, then passed to the LSTM model, and the output of the LSTM model is then converted back to text.

You can run this code by calling `python together.py` and it will execute the code and give the output as per the given dataset and model.

You can also use this code as a reference and adjust it as per your requirements.
