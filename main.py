#!/usr/bin/env python3
__author__ =  "Momar T. Cisse"

def main():
    """Main entry"""
    print('Hello...')

    ## Read the user input
    ## User will input of the # of names to generate
    num_names_to_generate = read_user_input()

    ## Train the model
    train_model()

    ## Generate the names using our model
    generate_names(num_names_to_generate)

def read_user_input():
    print("Reading user input...")
    user_input = input("How many names do you wish to generate?\n")
    return user_input

def train_model():
    print("Training model...")

def generate_names(num_of_names_to_generate):
    print(f"generating names {num_of_names_to_generate} names...")

if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()