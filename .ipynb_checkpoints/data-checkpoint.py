{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "filepath = os.path.join(\"Resources\", \"cities.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "cities_df = pd.read_csv(filepath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City_ID</th>\n",
       "      <th>City</th>\n",
       "      <th>Cloudiness</th>\n",
       "      <th>Country</th>\n",
       "      <th>Date</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Lat</th>\n",
       "      <th>Lng</th>\n",
       "      <th>Max Temp</th>\n",
       "      <th>Wind Speed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>jacareacanga</td>\n",
       "      <td>0</td>\n",
       "      <td>BR</td>\n",
       "      <td>1528902000</td>\n",
       "      <td>62</td>\n",
       "      <td>-6.22</td>\n",
       "      <td>-57.76</td>\n",
       "      <td>89.60</td>\n",
       "      <td>6.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>kaitangata</td>\n",
       "      <td>100</td>\n",
       "      <td>NZ</td>\n",
       "      <td>1528905304</td>\n",
       "      <td>94</td>\n",
       "      <td>-46.28</td>\n",
       "      <td>169.85</td>\n",
       "      <td>42.61</td>\n",
       "      <td>5.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>goulburn</td>\n",
       "      <td>20</td>\n",
       "      <td>AU</td>\n",
       "      <td>1528905078</td>\n",
       "      <td>91</td>\n",
       "      <td>-34.75</td>\n",
       "      <td>149.72</td>\n",
       "      <td>44.32</td>\n",
       "      <td>10.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>lata</td>\n",
       "      <td>76</td>\n",
       "      <td>IN</td>\n",
       "      <td>1528905305</td>\n",
       "      <td>89</td>\n",
       "      <td>30.78</td>\n",
       "      <td>78.62</td>\n",
       "      <td>59.89</td>\n",
       "      <td>0.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>chokurdakh</td>\n",
       "      <td>0</td>\n",
       "      <td>RU</td>\n",
       "      <td>1528905306</td>\n",
       "      <td>88</td>\n",
       "      <td>70.62</td>\n",
       "      <td>147.90</td>\n",
       "      <td>32.17</td>\n",
       "      <td>2.95</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   City_ID          City  Cloudiness Country        Date  Humidity    Lat  \\\n",
       "0        0  jacareacanga           0      BR  1528902000        62  -6.22   \n",
       "1        1    kaitangata         100      NZ  1528905304        94 -46.28   \n",
       "2        2      goulburn          20      AU  1528905078        91 -34.75   \n",
       "3        3          lata          76      IN  1528905305        89  30.78   \n",
       "4        4    chokurdakh           0      RU  1528905306        88  70.62   \n",
       "\n",
       "      Lng  Max Temp  Wind Speed  \n",
       "0  -57.76     89.60        6.93  \n",
       "1  169.85     42.61        5.64  \n",
       "2  149.72     44.32       10.11  \n",
       "3   78.62     59.89        0.94  \n",
       "4  147.90     32.17        2.95  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cities_df.head()"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
