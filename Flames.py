{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "62f5b02b-7f0d-42f0-96f3-e8d2051265de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "First Player Name :  steve\n",
      "Second Player Name :  peggy\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Relationship Status : Affectionate\n"
     ]
    }
   ],
   "source": [
    "def eliminateCommonChars(listOne, listTwo) :  \n",
    "    for i in range(len(listOne)) :  \n",
    "        for j in range(len(listTwo)) :  \n",
    "            if listOne[i] == listTwo[j] :  \n",
    "                c = listOne[i]  \n",
    "                listOne.remove(c)  \n",
    "                listTwo.remove(c)  \n",
    "                listThree = listOne + [\"*\"] + listTwo  \n",
    "                return [listThree, True]  \n",
    "  \n",
    "    listThree = listOne + [\"*\"] + listTwo  \n",
    "    return [listThree, False]  \n",
    "  \n",
    "# Driver code  \n",
    "if __name__ == \"__main__\" :  \n",
    "    playerOne = input(\"First Player Name : \")  \n",
    "    playerOne = playerOne.lower()  \n",
    "    playerOne.replace(\" \", \"\")  \n",
    "    playerOneList = list(playerOne)  \n",
    "  \n",
    "    playerTwo = input(\"Second Player Name : \")  \n",
    "    playerTwo = playerTwo.lower()  \n",
    "    playerTwo.replace(\" \", \"\")  \n",
    "    playerTwoList = list(playerTwo)  \n",
    "  \n",
    "    proceed = True  \n",
    "      \n",
    "    while proceed :  \n",
    "        retList = eliminateCommonChars(playerOneList, playerTwoList)  \n",
    "        conList = retList[0]  \n",
    "        proceed = retList[1]  \n",
    "        starIndex = conList.index(\"*\")  \n",
    "  \n",
    "        playerOneList = conList[ : starIndex]  \n",
    "        playerTwoList = conList[starIndex + 1 : ]  \n",
    "  \n",
    "    theCount = len(playerOneList) + len(playerTwoList)  \n",
    "  \n",
    "    # list of FLAMES acronym  \n",
    "    res = [\"Friends\", \"Lovers\", \"Affectionate\", \"Marriage\", \"Enemies\", \"Siblings\"]  \n",
    "  \n",
    "    while len(res) > 1 :  \n",
    "        splitIndex = (theCount % len(res) - 1)  \n",
    "        if splitIndex >= 0 :  \n",
    "            right = res[splitIndex + 1 : ]  \n",
    "            left = res[ : splitIndex]  \n",
    "            res = right + left  \n",
    "        else :  \n",
    "            res = res[ : len(res) - 1]  \n",
    "  \n",
    "    # print final result  \n",
    "    print(\"Relationship Status :\", res[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24cda3de-9109-464e-b523-22fea56191b6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
