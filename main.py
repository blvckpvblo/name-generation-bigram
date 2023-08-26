#!/usr/bin/env python3
__author__ =  "Momar T. Cisse"

## Imports
import torch
import torch.nn.functional as F

## Global vars
seed = 2147483647

def main():
    """Main entry"""
    ## Read the user input
    ## User will input of the # of names to generate
    num_names_to_generate = read_user_input()

    ## Read dataset for training names.txt
    dataset = read_raw_data()

    ## Create a lookup table for characters
    stoi, itos = create_lookup_table(dataset)

    ## Create the dataset
    xs, ys, num = create_network_dataset(dataset, stoi)

    ## Initialize our neural network
    W = init_network()

    ## Train the model
    W = train_model(xs, ys, num, W)

    ## Generate the names using our model
    generate_names(num_names_to_generate, W, itos)

def read_user_input():
    is_valid_input = False
    user_input = 0

    ## Validate that the value inputted by the user is valid
    while not is_valid_input:
        user_input = input("How many names do you wish to generate?\n")

        if not user_input.isdigit():
            print(f"{user_input} is not a valid number")
        else:
            is_valid_input = True
        
    return int(user_input)

def read_raw_data():
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

def create_network_dataset(dataset, stoi):
    print("Creating the dataset...")
    xs, ys = [], []

    for data in dataset:
        chs = ['.'] + list(data) + ['.']

        for ch1, ch2 in zip(chs, chs[1:]):
            ix1 = stoi[ch1]
            ix2 = stoi[ch2]
            xs.append(ix1)
            ys.append(ix2)

    xs = torch.tensor(xs)
    ys = torch.tensor(ys)
    num = xs.nelement()
    print('number of examples: ', num)

    return xs, ys, num

def init_network():
    print("Initializing neural network...")
    g = torch.Generator().manual_seed(seed)
    return torch.randn((27, 27), generator=g, requires_grad=True)

def train_model(xs, ys, num, W):
    print("Training model...")
    print("Starting gradient descent")
    # Gradient descent
    for _ in range(100):
        # forward pass
        xenc = F.one_hot(xs, num_classes=27).float()
        logits = xenc @ W
        counts = logits.exp()
        probs = counts / counts.sum(1, keepdims=True)
        loss = -probs[torch.arange(num), ys].log().mean()
        # print(loss.item())

        # Backward pass
        W.grad = None
        loss.backward()

        # Update
        W.data += -50 * W.grad # type: ignore
    
    return W

def generate_names(num_of_names_to_generate, W, itos):
    print(f"generating names {num_of_names_to_generate} names...")
    g = torch.Generator().manual_seed(seed)

    for _ in range(num_of_names_to_generate):
        out = []
        ix = 0

        while True:
            xenc = F.one_hot(torch.tensor([ix]), num_classes=27).float()
            logits = xenc @ W
            counts = logits.exp()
            p = counts / counts.sum(1, keepdims=True)

            ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
            out.append(itos[ix])
            if ix == 0:
                break

        print(''.join(out))

if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()