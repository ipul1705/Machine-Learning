{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.1.3\n",
      "1.19.2\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "print(pd.__version__)\n",
    "print(np.__version__)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   A  B  C  D  E\n",
      "0  3  4  6  8  6\n",
      "1  9  7  2  8  8\n",
      "2  9  7  8  8  8\n",
      "3  6  8  8  9  3\n",
      "4  4  9  9  4  6\n"
     ]
    }
   ],
   "source": [
    "n_rows = 5\n",
    "n_cols = 5\n",
    "\n",
    "cols = tuple('ABCDE')\n",
    "df = pd.DataFrame(np.random.randint(1,10, size= (n_rows, n_cols)), columns=cols)\n",
    "print (df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
