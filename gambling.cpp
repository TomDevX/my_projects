/**
 *    Welcome to gambling game 1.0
 **/

#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <unordered_map>

using namespace std;

// ===========================================================================

void blackjack(){
    vector<string> dealer;
    vector<string> player;
    cout << "Welcome to BlackJack";
    cout << "=======================" << endl;
    cout << "Rule: We will be the dealer, your objective is to get the cards which value is not over 21 and greater than the dealer total value!" << endl;
    cout << "========================" << endl;
    cout << "Dealer cards: ";
}

// ==========================================================================

int blackjack_random(){
    /**
    * Random algo
    **/
    unordered_map<string, int> cards = black_jack_cards();
    vector<string> deck;
    for(const auto& pair : cards){
        deck.push_back(pair.first);
    }

    random_device rd;                                  
    mt19937 gen(rd());                                  
    uniform_int_distribution<> dis(0, deck.size() - 1);
    int random_index = deck[]
}
unordered_map<string,int> black_jack_cards(){
    unordered_map<string, int> cards;
    cards["A"] = -1;
    cards["2"] = 2;
    cards["3"] = 3;
    cards["4"] = 4;
    cards["5"] = 5;
    cards["6"] = 6;
    cards["7"] = 7;
    cards["8"] = 8;
    cards["9"] = 9;
    cards["10"] = 10;
    cards["J"] = 10;
    cards["Q"] = 10;
    cards["K"] = 10;
    return cards;
}

// ===========================================================================


int main(){
    cout << "Welcome to our gambling game" << endl;
    cout << "===============================" << endl;
    blackjack();
}
