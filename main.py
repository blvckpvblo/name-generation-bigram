#!/usr/bin/env python3
__author__ =  "Momar T. Cisse"

def main():
    """Main entry"""
    ## Read the user input
    ## User will input of the # of names to generate
    num_names_to_generate = read_user_input()

    ## Read dataset for training names.txt
    dataset = read_training_dataset()

    ## Create a lookup table for characters
    stoi, itos = create_lookup_table(dataset)

    ## Train the model
    train_model()

    ## Generate the names using our model
    generate_names(num_names_to_generate)

def read_user_input():
    print("Reading user input...")
    user_input = input("How many names do you wish to generate?\n")
    
    return user_input

def read_training_dataset():
    print("Reading training dataset...")
    words = open('names.txt', 'r').read().splitlines()

    return words

def create_lookup_table(dataset):
    print("Create lookup table...")
    chars = sorted(list(set(''.join(dataset))))
    stoi = {s:i+1 for i,s in enumerate(chars)}
    stoi['.'] = 0
    itos = {i:s for s,i in stoi.items()}

    return stoi, itos

def train_model():
    print("Training model...")

def generate_names(num_of_names_to_generate):
    print(f"generating names {num_of_names_to_generate} names...")

if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()